import logging

from Scrapping.MovieScraping import movieClass
from Scrapping.ActorScraping import actorClass
from Graph.GraphLibrary import graphClass


class webScrapClass:

    def scrapActorInMovie(self, tempMovie, actorArr, actorQue):
        tempActorCount = 0
        tempActor = None
        for cast in tempMovie["C_Cast"]:
            # check if exist
            if not any(a["ActorName"] == cast["aName"] for a in actorArr):
                tempActor = actorClass().actorScarp(cast["aLink"])
            # if cannot resolve this actor, then go next
            if (tempActor == None):
                continue
            else:
                actorArr.append(tempActor)
                actorQue.append(tempActor)
                tempActorCount += 1
        return tempActorCount
# end of scrapActorInMovie

    def scrapMovieInActor(self, tempActor, movieArr, movieQue):
        tempMovieCount = 0
        tempMoive = None
        for movie in tempActor["Movies"]:
            if not any(m["A_MoviesName"] == movie["mName"] for m in movieArr):
                tempMoive = movieClass().movieScrap(movie["mLink"])
            # if cannot resolve this movie, then go next
            if (tempMoive == None):
                continue
            else:
                #check if exist
                movieArr.append(tempMoive)
                movieQue.append(tempMoive)
                tempMovieCount += 1
        return tempMovieCount
# end of scrapMovieInActor

    def webGoThrough(self, starturl):

        movieCount = 0
        actorCount = 0

        actorQueue = []
        movieQueue = []

        actorArr = []
        movieArr = []

        # Scrap Starting URL
        tempM = movieClass().movieScrap(starturl)
        if (tempM == None):
            logging.error("Start URL" + starturl + ' was not able to be parsed.')
            return None

        movieQueue.append(tempM)
        movieArr.append(tempM)
        movieCount += 1
        # Starting URL is woring begin while
        while (movieCount < 125 or actorCount < 125):
            # scrap all actors in the tempMovie

            while(len(movieQueue) != 0):
                tempM = movieQueue.pop(0)
                actorCount += self.scrapActorInMovie(tempM, actorArr, actorQueue)

            # go to next movie web from actor list and get JSON object
            if (len(actorQueue)!= 0):
                tempA = actorQueue.pop(0)
                movieCount += self.scrapMovieInActor(tempA, movieArr, movieQueue)

            if (len(actorQueue)==0 and len(movieQueue) == 0):
                print("no element in queue")
                break


        webMoviesJSON = {
            "Movies": movieArr
        }


        webActorJSON = {
            "Actors": actorArr
        }

        graphClass().DataToJson(webMoviesJSON, "webMoviesJSON")
        graphClass().DataToJson(webActorJSON,"webActorJSON")


        print(movieCount)
        print(actorCount)
import json
import logging
import os.path


class graphClass:

    GRAPH_LOG = 'graphLogFile.log'
    logging.basicConfig(filename=GRAPH_LOG)

    def DataToJson(self,data,filename):

        with open(filename+'.json', 'w') as fpA:
            json.dump(data, fpA, sort_keys=True, indent=2, separators=(',', ': '))


    def JsonToData(self,jsonFile):

        with open(jsonFile, 'r') as file:
            return json.load(file)

# 1. Find how much a movie has grossed
    def movieGrossde(self, mName):

        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/webMoviesJSON.json')


        dataM = self.JsonToData(filename)

        for m in dataM["Movies"]:
            if (m["A_MoviesName"] == mName):
                return m["B_BoxOffice"]

        logging.error('Cannot find the movie ' + mName + ' in JSON')
        return None


# 2. List which movies an actor has worked in

    def actorMovies(self, aName):

        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/webActorJSON.json')

        dataA = self.JsonToData(filename)

        actorMovie = []

        for m in dataA["Actors"]:
            if (m["ActorName"] == aName):
                for movie in m["Movies"]:
                    actorMovie.append(movie["mName"])

        if(len(actorMovie) == 0):
            logging.error('Cannot find the actor ' + aName + ' in JSON')
            return None

        #print(aName + " worked in ")
        #print(actorMovie)
        return actorMovie

# 3. List which actors worked in a movie

    def movieCast(self, mName):

        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/webMoviesJSON.json')

        dataM = self.JsonToData(filename)

        castList = []

        for m in dataM["Movies"]:
            if (m["A_MoviesName"] == mName):
                for a in m["C_Cast"]:
                    castList.append(a["aName"])

        if (len(castList) == 0):
            logging.error('Cannot find the movie ' + mName + ' in JSON')
            return None

        return castList

# 4. List the top X actors with the most total grossing value
    def topGross(self, x):

        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/webMoviesJSON.json')

        dataM = self.JsonToData(filename)

        tempActorList = []

        for m in dataM["Movies"]:
            gValue = 0
            if m["B_BoxOffice"] != None:
                gValue = m["B_BoxOffice"]
            for c in m["C_Cast"]:
                exist = False
                # check if exist
                for act in tempActorList:
                    if act["name"] == c["aName"]:
                        exist = True
                        act["value"] += gValue
                # end of check loop
                if (exist == False):
                    tempActor = {
                        "name": c["aName"],
                        "value": gValue
                    }
                    tempActorList.append(tempActor)

        sortedValue = sorted(tempActorList, key=lambda k: k["value"])
        topX = []
        for i in range(1,x):
            topX.append(sortedValue[len(sortedValue)-i])

        return topX



# 5. List the oldest X actors

    def actorAgeList(self, x):

        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/webActorJSON.json')

        dataA = self.JsonToData(filename)

        ageList = []
        newData = []

        for a in dataA['Actors']:
            if (a["B_year"] != None):
                newData.append(a)

        sortedData = sorted(newData, key = lambda k: k["B_year"])
        for i in range(0,x):
            tempActor = {
                        "name": sortedData[i]["ActorName"],
                        "born year": sortedData[i]["B_year"],
                        }
            ageList.append(tempActor)


        return ageList

# 6. List all the movie for a given year
    def movieGivenYear(self, year):

        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/webMoviesJSON.json')

        dataM = self.JsonToData(filename)

        movieList = []

        for a in dataM["Movies"]:
            if (a["D_Year"] != None and a["D_Year"] == year):
                tempMovie = {
                    "name": a["A_MoviesName"],
                    "release year": a["D_Year"],
                }
                movieList.append(tempMovie)

        if(len(movieList) == 0):
            logging.error('No Movie in Given Year')
            return None

        return movieList


# 7. List all the actors for a given year
    def actorGivenYear(self, year):

        scriptpath = os.path.dirname(__file__)
        filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/webActorJSON.json')

        dataA = self.JsonToData(filename)

        actorList = []

        for a in dataA["Actors"]:
            if (a["B_year"] != None and a["B_year"] == year):
                tempActor = {
                    "name": a["ActorName"],
                    "born year": a["B_year"],
                }
                actorList.append(tempActor)

        if(len(actorList) == 0):
            logging.error('No Actor in Given Year')
            return None

        return actorList



# Source: http://stackoverflow.com/questions/25924720/filenotfounderror-errno-2
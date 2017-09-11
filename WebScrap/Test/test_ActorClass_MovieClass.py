import urllib
import urllib.request
from unittest import TestCase
from bs4 import BeautifulSoup

from Scrapping.MovieScraping import movieClass
from Scrapping.ActorScraping import actorClass
from Graph.GraphLibrary import graphClass


class TestActorClass(TestCase):

    def test_actorScarp(self):
        s = actorClass()
        self.assertRaises(Exception)

        testString = ["https://en.wikipedia.org/wiki/Woody_Harrelson",
                      "https://en.wikipedia.org/wiki/Jesse_Eisenberg",
                      "https://en.wikipedia.org/wiki/Now_You_See_Me_2",
                      "https://en.wikipedia.org/wiki/Morgan_Freeman"]
        actorArr = []

        for string in testString:
            actorInfo = actorClass().actorScarp(string)
            if (actorInfo != None):
                actorArr.append(actorInfo)


        actors = {
            "Actors": actorArr
        }

        graphClass().DataToJson(actors,"actors")

        data = graphClass().JsonToData("actors.json")


        self.assertEqual("Woody Harrelson", data["Actors"][0]["ActorName"])
        self.assertEqual("Jesse Eisenberg", data["Actors"][1]["ActorName"])

        self.assertEqual("Wildcats (film)", data["Actors"][0]["Movies"][0]["mName"])
        self.assertEqual("The Emperor's Club", data["Actors"][1]["Movies"][1]["mName"])

        self.assertEqual(None, actorClass().actorScarp(testString[2]))
# end of actor class test

class TestMovieClass(TestCase):
    def test_movieScarp(self):
        m = movieClass()
        self.assertRaises(Exception)

        testString2 = ["https://en.wikipedia.org/wiki/Now_You_See_Me_2",
                       "https://en.wikipedia.org/wiki/Jesse_Eisenberg",
                       "https://en.wikipedia.org/wiki/Roger_Dodger_(film)"]
        movieArr = []

        for string2 in testString2:
            movieInfo = movieClass().movieScrap(string2)
            if (movieInfo != None):
                movieArr.append(movieInfo)

        movies = {
            "Movies": movieArr
        }

        graphClass().DataToJson(movies,"movies")

        data2 = graphClass().JsonToData("movies.json")


        self.assertEqual(334900000.0, data2["Movies"][0]["B_BoxOffice"])
        self.assertEqual(1934497.0, data2["Movies"][1]["B_BoxOffice"])

        self.assertEqual(2016, data2["Movies"][0]["D_Year"])
        self.assertEqual(2002, data2["Movies"][1]["D_Year"])


        self.assertEqual("Now You See Me 2", data2["Movies"][0]["A_MoviesName"])
        self.assertEqual("Roger Dodger (film)", data2["Movies"][1]["A_MoviesName"])

        self.assertEqual("Jesse Eisenberg", data2["Movies"][0]["C_Cast"][0]["aName"])
        self.assertEqual("Isabella Rossellini", data2["Movies"][1]["C_Cast"][1]["aName"])

        self.assertEqual(None, movieClass().movieScrap(testString2[1]))
# end of movie class test


class TestWeb(TestCase):
    weburl = "https://en.wikipedia.org/wiki/Morgan_Freeman"
    webPage = urllib.request.urlopen(weburl)
    web = BeautifulSoup(webPage, "lxml")

    #print(web)


    # Source: https://confluence.jetbrains.com/display/PYH/Creating+and+running+a+Python+unit+test#CreatingandrunningaPythonunittest-CreatingasimplePythonproject
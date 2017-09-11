from unittest import TestCase

from Graph.DataGraphLib import dataGraphClass


class TestDataGraphClass(TestCase):


    def test_LoadActorData(self):
        d = dataGraphClass()
        self.assertRaises(Exception)


        actorList = dataGraphClass().LoadActorData("data.json")
        print(actorList)



    def test_LoadMovieData(self):
        d = dataGraphClass()
        self.assertRaises(Exception)


        movieList = dataGraphClass().LoadMovieData("data.json")
        print(movieList)



    def text_DrawGraph(self):
        d = dataGraphClass()
        self.assertRaises(Exception)

        actorList = dataGraphClass().LoadActorData("data.json")
        movieList = dataGraphClass().LoadMovieData("data.json")

        dataGraphClass().DrawGrph(actorList,movieList)




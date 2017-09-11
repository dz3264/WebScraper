import json
from unittest import TestCase

from Scrapping.WebScraping import webScrapClass


class TestWebScrapClass(TestCase):
    def test_scrapActorInMovie(self):
        sa = webScrapClass()
        self.assertRaises(Exception)

    def test_scrapMovieInActor(self):
        sw = webScrapClass()
        self.assertRaises(Exception)

    def test_webGoThrough(self):
        st = webScrapClass()
        self.assertRaises(Exception)


class TestwebScrapClass(TestCase):
    def test_webGoThrough(self):
        s = webScrapClass()
        self.assertRaises(Exception)

        start = "https://en.wikipedia.org/wiki/Now_You_See_Me_2"
        webScrapClass().webGoThrough(start)

        with open('webActorJSON.json', 'r') as fileA:
            dataA = json.load(fileA)
        self.assertEqual("Woody Harrelson", dataA["Actors"][2]["ActorName"])
        self.assertEqual("Superbad (film)", dataA["Actors"][3]["Movies"][0]["mName"])

        with open('webMoviesJSON.json', 'r') as fileM:
            dataM = json.load(fileM)
        self.assertEqual("The Emperor's Club", dataM["Movies"][2]["A_MoviesName"])
        self.assertEqual("Laura Linney", dataM["Movies"][4]["C_Cast"][1]["aName"])


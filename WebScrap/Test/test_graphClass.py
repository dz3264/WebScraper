from unittest import TestCase

from Graph.GraphLibrary import graphClass


class TestGraphClass(TestCase):

    def test_movieGrossde(self):
        s = graphClass()
        self.assertRaises(Exception)

        grossedNYSM2 = graphClass().movieGrossde("Now You See Me 2")
        grossedAdvLand = graphClass().movieGrossde("Adventureland (film)")
        grossedNull = graphClass().movieGrossde("Hello World")

        print("Now You See Me 2 's Box Office")
        print(grossedNYSM2)
        print("Adventureland (film) 's Box Office")
        print(grossedAdvLand)

        self.assertEqual(334900000.0, grossedNYSM2)
        self.assertEqual(17200000.0, grossedAdvLand)
        self.assertEqual(None, grossedNull)

    def test_actorMovies(self):
        s = graphClass()
        self.assertRaises(Exception)

        movieListJE = graphClass().actorMovies("Jesse Eisenberg")
        movieListLC = graphClass().actorMovies("Lizzy Caplan")
        movieListNull = graphClass().actorMovies("Hello World")

        print("Jesse Eisenberg's Movies List")
        print(movieListJE)
        print("Lizzy Caplan's Movies List")
        print(movieListLC)

        self.assertEqual("The Squid and the Whale", movieListJE[3])
        self.assertEqual("My Best Friend's Girl (2008 film)", movieListLC[4])
        self.assertEqual(None, movieListNull)

    def test_movieCast(self):
        s = graphClass()
        self.assertRaises(Exception)

        cast1 = graphClass().movieCast("The Squid and the Whale")
        cast2 = graphClass().movieCast("The Hunger Games (film)")
        castNull = graphClass().movieCast("Hello World")

        print("The Squid and the Whale's Cast List")
        print(cast1)
        print("The Hunger Games (film)'s Cast List")
        print(cast2)

        self.assertEqual("Jeff Daniels", cast1[0])
        self.assertEqual("Liam Hemsworth", cast2[2])
        self.assertEqual(None, castNull)

    def test_actorAgeList(self):
        s = graphClass()
        self.assertRaises(Exception)

        age5 = graphClass().actorAgeList(5)
        age20 = graphClass().actorAgeList(20)

        print(age5)
        print(age20)

        self.assertEqual("Lauren Bacall", age5[0]["name"])
        self.assertEqual("Ned Beatty", age20[10]["name"])


    def test_actorGivenYear(self):
        s = graphClass()
        self.assertRaises(Exception)


        ageList1930 = graphClass().actorGivenYear(1930)
        ageList1986 = graphClass().actorGivenYear(1986)
        ageListNone = graphClass().actorGivenYear(2019)

        print(ageList1930)
        print(ageList1986)

        self.assertEqual(3, len(ageList1930))
        self.assertEqual(None, ageListNone)


    def test_movieGivenYear(self):
        s = graphClass()
        self.assertRaises(Exception)


        mList2002 = graphClass().movieGivenYear(2002)
        mList2016 = graphClass().movieGivenYear(2016)
        mListNone = graphClass().actorGivenYear(2019)

        print(mList2002)
        print(mList2016)

        self.assertEqual("Roger Dodger (film)", mList2002[0]["name"])
        self.assertEqual(None, mListNone)


    def test_topGross(self):
        s = graphClass()
        self.assertRaises(Exception)

        top5 = graphClass().topGross(5)
        top20 = graphClass().actorAgeList(20)

        print("TOP 5")
        print(top5)

        print("TOP 20")
        print(top20)

        self.assertEqual("Woody Harrelson", top5[0]["name"])
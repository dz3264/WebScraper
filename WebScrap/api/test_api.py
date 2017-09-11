import os.path
import json
import api
import app
import unittest
from flask import Flask
from flask_testing import TestCase


class apiTest(unittest.TestCase):

    def setUp(self):
        api.app.config['Testing'] = True
        self.app = api.app.test_client()

    def test_hello(self):
        resp = self.app.get('/')

        assert "200 OK" == resp.status
        assert 'Hello World!' in str(resp.data)

#### TEST GET #####

    def test_filterActorName(self):
        response = self.app.get('/actorsName/Bruce')
        actorList = json.loads(response.get_data(as_text=True))

        assert 'Bruce Willis' in actorList['Actors'][0] or 'Bruce Willis' in actorList['Actors'][1]
        assert 'Bruce Dern' in actorList['Actors'][0] or 'Bruce Dern' in actorList['Actors'][1]

    def test_filterActorAge(self):
        response = self.app.get('/actorsAge/58')
        actorList = json.loads(response.get_data(as_text=True))

        assert 9 == len(actorList['Actors'])

        for i in range(0,8):
            k = actorList['Actors'][i].keys()
            assert 58 == actorList['Actors'][i][list(k)[0]]['age']


    def test_filterMovieName(self):
        response = self.app.get('/movieName/The')
        movieList = json.loads(response.get_data(as_text=True))

        assert 82 == len(movieList['Movie'])

        for i in range(0,81):
            k = movieList['Movie'][i].keys()
            assert 'The' in list(k)[0]

    def test_filterMovieYear(self):
        response = self.app.get('/movieYear/1996')
        movieList = json.loads(response.get_data(as_text=True))

        for i in range(0,len(movieList['Movie'])-1):
            k = movieList['Movie'][i].keys()
            assert 1996 == movieList['Movie'][i][list(k)[0]]['year']

    def test_getActorName(self):
        response = self.app.get('/actors/Liv_Tyler')
        actor = json.loads(response.get_data(as_text=True))

        k = actor.keys()

        assert 'Liv Tyler' == list(k)[0]
        assert 39 == actor[list(k)[0]]['age']


    def test_getActorAge(self):

        response = self.app.get('/actors/35')
        actor = json.loads(response.get_data(as_text=True))

        k = actor.keys()
        assert 35 == actor[list(k)[0]]['age']


    def test_getMovieName(self):

        response = self.app.get('/movies/Midnight_Crossing')
        movie = json.loads(response.get_data(as_text=True))

        k = movie.keys()
        assert 'Midnight Crossing' == list(k)[0]
        assert 1988 == movie[list(k)[0]]['year']

    def test_getMovieYear(self):

        response = self.app.get('/movies/1990')
        movie = json.loads(response.get_data(as_text=True))
        print(movie)

        k = movie.keys()
        assert 1990 == movie[list(k)[0]]['year']



if __name__ == '__main__':
    unittest.main()


# Source: https://www.youtube.com/watch?v=APbPtQg3_04
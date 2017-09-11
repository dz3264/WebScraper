from flask import Flask, request, jsonify, abort
import os.path
import json

app = Flask(__name__)

scriptpath = os.path.dirname(__file__)
filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/data.json')
with open(filename, 'r') as file:
    data = json.load(file)

actors = data[0]
movies = data[1]


@app.route("/")
def hello():
    return "Hello World!"

########################## GET ##########################

# Actor Fliter By Name
@app.route('/actorsName/<string:actor_name>',methods=['GET'])
def filterActorName(actor_name):
    actor = []

    for keyA, valueA in actors.items():
        if actor_name in keyA:
            actor.append({keyA:valueA})

    if len(actor) == 0:
        abort(404)
    return jsonify({'Actors': actor})


# Actor Fliter By Age
@app.route('/actorsAge/<int:actor_age>',methods=['GET'])
def filterActorAge(actor_age):
    actor = []
    for keyA, valueA in actors.items():
        if actor_age == valueA['age']:
            actor.append({keyA:valueA})

    if len(actor) == 0:
        abort(404)
    return jsonify({'Actors': actor})

# Movie Fliter By Name
@app.route('/movieName/<string:movie_name>',methods=['GET'])
def filterMovieName(movie_name):
    movie = []
    for keyM, valueM in movies.items():
        if movie_name in keyM:
            movie.append({keyM:valueM})

    if len(movie) == 0:
        abort(404)
    return jsonify({'Movie': movie})


# Movie Fliter By Year
@app.route('/movieYear/<int:movie_year>',methods=['GET'])
def filterMovieYear(movie_year):
    movie = []
    for keyM, valueM in movies.items():
        if movie_year == valueM['year']:
            movie.append({keyM: valueM})

    if len(movie) == 0:
        abort(404)
    return jsonify({'Movie': movie})


# Get Actor By Name
@app.route('/actors/<string:actor_name>',methods=['GET'])
def getActorName(actor_name):
    getActor = None
    parseName = actor_name.split("_")

    tempname = parseName[0] + " "
    for i in range(1,len(parseName)-1):
        tempname += parseName[i] + " "
    name = tempname + parseName[len(parseName)-1]

    for keyA, valueA in actors.items():
        if name == keyA:
            getActor = {keyA:valueA}
            break

    if getActor == None:
        abort(404)
    return jsonify(getActor)


# Get Actor By Age
@app.route('/actors/<int:actor_age>',methods=['GET'])
def getActorAge(actor_age):
    getActor = None

    for keyA, valueA in actors.items():
        if actor_age == valueA['age']:
            getActor = {keyA:valueA}
            break

    if getActor == None:
        abort(404)
    return jsonify(getActor)


# Get Movie By Name
@app.route('/movies/<string:movie_name>',methods=['GET'])
def getMovieName(movie_name):
    getMovie = None
    parseName = movie_name.split("_")

    tempname = parseName[0] + " "
    for i in range(1,len(parseName)-1):
        tempname += parseName[i] + " "
    name = tempname + parseName[len(parseName)-1]

    for keyM, valueM in movies.items():
        if name == keyM:
            getMovie = {keyM:valueM}
            break

    if getMovie == None:
        abort(404)
    return jsonify(getMovie)


# Get Movie By Year
@app.route('/movies/<int:movie_year>',methods=['GET'])
def getMovieYear(movie_year):
    getMovie = None

    for keyM, valueM in movies.items():
        if movie_year == valueM['year']:
            getMovie = {keyM:valueM}
            break

    if getMovie == None:
        abort(404)
    return jsonify(getMovie)

########################## PUT ##########################
@app.route('/actors/<string:actor_name>', methods=['PUT'])
def updateActor(actor_name):

    actor = []
    parseName = actor_name.split("_")
    tempname = parseName[0] + " "
    for i in range(1, len(parseName) - 1):
        tempname += parseName[i] + " "
    name = tempname + parseName[len(parseName) - 1]

    for keyA, valueA in actors.items():
        if name == keyA:
            actor.append({keyA:valueA})


    if len(actor) == 0:
        abort(404)

    actor[0][name]['total_gross'] = request.json['total_gross']

    return jsonify({'actor' : actor[0]})

@app.route('/movies/<string:movie_name>', methods=['PUT'])
def updateMovie(movie_name):

    movie = []
    parseName = movie_name.split("_")
    tempname = parseName[0] + " "
    for i in range(1, len(parseName) - 1):
        tempname += parseName[i] + " "
    name = tempname + parseName[len(parseName) - 1]

    for keyM, valueM in movies.items():
        if name == keyM:
            movie.append({keyM:valueM})

    if len(movie) == 0:
        abort(404)

    movie[0][name]['box_office'] = request.json['box_office']

    return jsonify({'movie' : movie[0]})

########################## POST ##########################

@app.route('/actors', methods=['POST'])
def addActor():

    actor = {'name' : request.json['name']}

    actors[request.json['name']]= actor

    return jsonify({'actor' : actor})

@app.route('/movies', methods=['POST'])
def addMovie():

    movie = {'name': request.json['name']}

    movies[request.json['name']] = (movie)

    return jsonify({'movie' : movie})


########################## DELETE ##########################
@app.route('/actors/<string:actor_name>', methods=['DELETE'])
def deleteActor(actor_name):
    actor = []
    parseName = actor_name.split("_")
    tempname = parseName[0] + " "
    for i in range(1, len(parseName) - 1):
        tempname += parseName[i] + " "
    name = tempname + parseName[len(parseName) - 1]

    for keyA, valueA in actors.items():
        if name == keyA:
            actor.append({keyA: valueA})

    if len(actor) == 0:
        abort(404)

    actors.pop(name)


    return jsonify({'result': True})

@app.route('/movies/<string:movie_name>', methods=['DELETE'])
def deleteMovie(movie_name):

    movie = []
    parseName = movie_name.split("_")
    tempname = parseName[0] + " "
    for i in range(1, len(parseName) - 1):
        tempname += parseName[i] + " "
    name = tempname + parseName[len(parseName) - 1]

    for keyM, valueM in movies.items():
        if name == keyM:
            movie.append({keyM:valueM})

    if len(movie) == 0:
        abort(404)

    movies.pop(name)

    return jsonify({'movie' : movie[0]})



if __name__ == '__main__':
    app.run()





# Source: https://www.youtube.com/watch?v=2gunLuqHvc8
# Source: https://www.youtube.com/watch?v=9ql0uA6ziJs
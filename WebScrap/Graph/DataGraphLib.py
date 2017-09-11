import json
import logging
import os.path

import matplotlib.pyplot as plt
import networkx as nx


class dataGraphClass:

    DATA_LOG = 'dataLogFile.log'
    logging.basicConfig(filename=DATA_LOG)

## Load Actors Data
    def LoadActorData(self,jsonFile):

        with open(jsonFile, 'r') as file:
            data =  json.load(file)

        # list to set actors & movies data from json file
        # get subgraph first
        Actors = []

        # Go through and create Actor Node
        for keyA, valueA in data[0].items():
            tempActor = {
                "ActorName": keyA,
                "ActorAge": valueA['age'],
                "ActorTotalGross": valueA['total_gross']
            }
            Actors.append(tempActor)

        return Actors

## Load Movie Data

    def LoadMovieData(self, jsonFile):

        with open(jsonFile, 'r') as file:
            data = json.load(file)

        # list to set actors & movies data from json file
        # get subgraph first

        Movies = []

        # Go through and create Actor Node

            # Go through and create Movie Node
        for keyM, valueM in data[1].items():
            tempMovie = {
                    "MovieName": keyM,
                    "GrossValue": valueM['box_office'],
                    "Actors": valueM['actors']
                }
            Movies.append(tempMovie)

        return Movies

## get subgraph

    def getSubgraph(self, allActors, allMovies, num):
        #print("getSubgraph")

        subActor = []
        actorNames = []
        subMovies = []

        # get subgraph of movies
        for mov in allMovies:
            ActorCount = 0
            # Check if movies have actor list
            if len(mov['Actors']) != 0:
                # Check if there enough actor can create edges
                for actors in mov['Actors']:
                    for key in allActors:
                        if(actors == key['ActorName']):
                            actorNames.append(actors)
                            ActorCount += 1
                if ActorCount >= 3:
                    subMovies.append(mov)

                else:
                    while (ActorCount != 0):
                        actorNames.pop()
                        ActorCount -= 1

            if len(subMovies) >= num:
                break



        # get subgraph of actor
        for act in allActors:
            if act['ActorName'] in actorNames:
                subActor.append(act)

            if len(subActor) >= num:
                break


        subgraph = [subActor, subMovies]
        return subgraph


## Create the graph structure
    def CreateGraph(self, actorNodeList, movieNodeList):
        G = nx.Graph()

        ActorNodes = []

        #print("Actor:")
        # get actor node into graph
        for act in actorNodeList:
            G.add_node(act['ActorName'])
            G.node[act['ActorName']]['ActorName'] = act['ActorName']
            G.node[act['ActorName']]['ActorAge'] = act['ActorAge']
            G.node[act['ActorName']]['ActorGross'] = act['ActorTotalGross']
            G.node[act['ActorName']]['Label'] = act['ActorName'] + ", " + str(act['ActorAge'])
            G.node[act['ActorName']]['Type'] = "Actor"
            ActorNodes.append(act['ActorName'])
        #print(ActorNodes)

        #print("Movie:")
        # get movie node into graph
        for mov in movieNodeList:
            G.add_node(mov['MovieName'])
            G.node[mov['MovieName']]['MovieName'] = mov['MovieName']
            G.node[mov['MovieName']]['GrossValue'] = mov['GrossValue']
            G.node[mov['MovieName']]['Label'] = mov['MovieName'] + ", " + str(mov['GrossValue'])
            G.node[mov['MovieName']]['Type'] = "Movie"
        #print(MovieNodes)


        for movEdge in movieNodeList:
            for i in range(0,len(movEdge['Actors'])):
                if movEdge['Actors'][i] in ActorNodes:
                    G.add_edge(movEdge['MovieName'], movEdge['Actors'][i], weight=len(movEdge['Actors'])-i)

        return G

## Draw the graph
    def DrawGraph(self,G):
        ActorNodes = []
        MovieNodes = []

        for nodeName in G.nodes():

            if G.node[nodeName]['Type'] == "Actor":
                ActorNodes.append(G.node[nodeName]['ActorName'])
            else:
                MovieNodes.append(G.node[nodeName]['MovieName'])

        pos = nx.circular_layout(G)

        nx.draw(G, pos)

        node_labels = nx.get_node_attributes(G, 'Label')
        #print(node_labels)
        nx.draw_networkx_labels(G, pos, labels=node_labels)

        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # color actor nodes blue
        nx.draw_networkx_nodes(G, pos, nodelist=ActorNodes, node_color="b")

        # color movie nodes red
        nx.draw_networkx_nodes(G, pos, nodelist=MovieNodes, node_color="r")

        plt.show()




# creatw connection graph
    def CreateConnectGraph(self,ActorList,MovieList):
        G = nx.Graph()

        # get actor node into graph
        for act in ActorList:
            G.add_node(act['Name'])
            G.node[act['Name']]['Connection'] = act['Connection']
            G.node[act['Name']]['Label'] = act['Name'] + ", " + str(act['Connection'])


        #G.add_edge("Terrence Howard", "Cheryl Chase", weight=5)

        for movEdge in MovieList:
            for i in range(0,len(movEdge['ActorIn'])):
                for j in range(i+1,len(movEdge['ActorIn'])):
                    G.add_edge(movEdge['ActorIn'][i], movEdge['ActorIn'][j], movie = movEdge['Name'])

        return G



scriptpath = os.path.dirname(__file__)
filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/data.json')

actorList = dataGraphClass().LoadActorData(filename)
movieList = dataGraphClass().LoadMovieData(filename)


subgraph = dataGraphClass().getSubgraph(actorList, movieList,15)

#print(subgraph[1])

G = dataGraphClass().CreateGraph(subgraph[0], subgraph[1])

#dataGraphClass().DrawGraph(G)




# Source Cite: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html





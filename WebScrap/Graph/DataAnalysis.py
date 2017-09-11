from Graph.DataGraphLib import dataGraphClass
import os.path
import networkx as nx
import matplotlib.pyplot as plt


class analysisClass:

#Who are the "hub" actors in your dataset?
    def hubActor(self, actorList, movieList):


        graph = dataGraphClass().CreateGraph(actorList, movieList)

        ActorList = []
        MovieList = []
        ActorNodes = []
        MovieNodes = []

        # get all ActorNode and MovieNode
        for nodeName in graph.nodes():

            if graph.node[nodeName]['Type'] == "Actor":
                ActorNodes.append(graph.node[nodeName])
            else:
                MovieNodes.append(graph.node[nodeName])

        # count connect of actors
        hub = ActorNodes[0]
        maxConnect = 0

        for node in ActorNodes:
            movieIn = graph.neighbors(node['ActorName'])
            movieConnect = 0
            for m in movieIn:

                movieConnect += graph.degree(m) -1
                actorIn = graph.neighbors(graph.node[m]['MovieName'])

                tempMovie = {
                    "Name": m,
                    "ActorIn" : actorIn
                }
                if tempMovie not in MovieList:
                    MovieList.append(tempMovie)



            tempActor = {
                        "Name" : node['ActorName'],
                        "Connection" : movieConnect,
                        "Movies": movieIn
                        }
            print(tempActor['Name'])
            if(movieConnect>100):
                print(movieConnect)

            ActorList.append(tempActor)

            if maxConnect < movieConnect:
                maxConnect = movieConnect
                hub = tempActor

        #print(hub)
        # Draw the connection graph
        hubActorG = dataGraphClass().CreateConnectGraph(ActorList,MovieList)

        pos = nx.circular_layout(hubActorG)
        nx.draw(hubActorG, pos)

        # print(node_labels)
        node_labels = nx.get_node_attributes(hubActorG, 'Label')
        nx.draw_networkx_labels(hubActorG, pos, labels=node_labels)

        edge_labels = nx.get_edge_attributes(hubActorG, 'movie')
        nx.draw_networkx_edge_labels(hubActorG, pos, labels=edge_labels)

        plt.show()

# Is there an age group that generates the most amount of money? What does the correlation between age and grossing value look like?
    def ageGroupMoney(self, actorList):

        AgeList = []

        for act in actorList:
            age = act['ActorAge']
            gross = act['ActorTotalGross']
            exist = False
            #already exist
            for a in AgeList:
                if a['Age'] == age:
                    a['Gross'] += gross
                    exist = True

            # After loop still no that age record
            if exist == False:
                temp = {
                    "Age": age,
                    "Gross": gross
                }
                AgeList.append(temp)


        sorted_AgeList = sorted(AgeList, key=lambda k: k['Age'])
        #print(sorted_AgeList)

        # draw the histogram of age gross
        ageX = [item['Age'] for item in sorted_AgeList]
        grossY = [it['Gross'] for it in sorted_AgeList]
        print(grossY[0])

        plt.plot(ageX, grossY, 'ro')
        plt.axis([-1, 100, 0, max(grossY)])

        plt.xlabel('Age Group')
        plt.ylabel('Total Gross')
        plt.title('Age Group Generates Money')

        plt.show()




scriptpath = os.path.dirname(__file__)
filename = os.path.join(os.path.abspath(os.path.join(scriptpath, os.pardir)), 'Test/data.json')

actorList = dataGraphClass().LoadActorData(filename)
movieList = dataGraphClass().LoadMovieData(filename)

subgraph = dataGraphClass().getSubgraph(actorList, movieList, 15)

analysisClass().hubActor(actorList, movieList)
#analysisClass().hubActor(subgraph[0], subgraph[1])

#analysisClass().ageGroupMoney(actorList)
#analysisClass().ageGroupMoney(subgraph[0])
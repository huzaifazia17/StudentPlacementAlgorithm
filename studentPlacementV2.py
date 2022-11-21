# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
   
  
# Defining a Class
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G, node_size=1000)
        plt.show()

def readPreferences(filename):
    preferences = {}
    with open(filename) as f:
        keys = f.readline().split(",")
        keys = keys[:-1]  # Remove \n from end of line
        for line in f: #TEST
            line = line[:-1]  # Remove \n from end of line
            values = line.split(",")
            for i in range(len(keys)):
                key = keys[i]
                value = values[i]
                if key in preferences:
                    preferences[key].append(value)
                else:
                    preferences[key] = [value]
    return preferences

def generateGraph(graph, dictionary):
    for key, valueList in dictionary.items():
        for value in valueList:
            graph.addEdge(key, value)

schoolPreferences = "school-preferences.txt"
studentPreferences = "student-preferences.txt"

# Passes filenames to function which returns the generated dictionary
schoolPref = readPreferences(schoolPreferences)
studentPref = readPreferences(studentPreferences)
    
G = GraphVisualization()

generateGraph(G, schoolPref)
# generateGraph(G, studentPref)


G.visualize()

""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""
class Graph_class(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object """           
        
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.   
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1,vertex2):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        
        if vertex1 in self.graph_dict:
            """To avoid duplicate addition of edges"""
            if vertex2 not in self.graph_dict[vertex1]:
                self.graph_dict[vertex1].append(vertex2)
                
        else:            
            self.graph_dict[vertex1] = [vertex2]
               

    def generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    def Find_nbours(self,vertex1):
        return self.graph_dict[vertex1] 
        
    def Vertices_on_edge(self,edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        [vertex1, vertex2] = list(edge)
        
        if vertex1 in self.graph_dict.keys():
            if vertex2 in self.graph_dict[vertex1]:
                return vertex1,vertex2
        else:
            print('no such edge')
    


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["d"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["f"],
          "f" : []
        }


    graph = Graph_class(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.add_edge("a","z")
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge("x","y")
    print("Edges of graph:")
    print(graph.edges())

    print('Neighbours of vertex a:')
    print(graph.Find_nbours("a"))

    print('vertices on edge {"x","y"}')
    print(graph.Vertices_on_edge(["x","y"]))

class Vertex:
    def __init__(self,value):
        self.value = value
        self.edges = {} #Dictionary allows for weighted values for each edge
    
    def addEdge(self,newVertex,weight=0):
        if(newVertex not in self.edges):
            self.edges[newVertex] = weight

    def getEdges(self):
        pass

#Graph takes a list of vertices
class Graph:
    def __init__(self,vertices,isDirected=False):
        self.vertices = vertices

    def addVertex(self):
        pass

    def addEdge(self,from_vertex, to_vertex, weight=0):
        pass
    def findPath(self, start, end):
        pass


v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)

#Add weighted edges between vertices
v1.addEdge(v2,3)
v2.addEdge(v3,5)
v3.addEdge(v4,2)
v4.addEdge(v2,10)

graph = Graph()
graph.addVertex()
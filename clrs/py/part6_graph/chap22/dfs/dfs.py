import enum
from collections import namedtuple

class Vertex:
    def __init__(self,name):
        self.edges = []
        self.name = name
        self.id = -1  # unintialized id
    def addEdge(self,v):
        self.edges.append(v)
        return self
    def getEdge(self,idx):
        return self.edges[idx]
    def getNumEdges(self):
        return len(self.edges)
    def getName(self):
        return self.name

class AdjGraph:

    @classmethod
    def CreateGraphFromDict(cls,graph_data, undirected = False):
        g = AdjGraph(undirected)
        for v in graph_data:
            g.addVertex(v)
        for u in graph_data:
            edges = graph_data[u]
            # add edge (u,v)
            for v in edges:
                g.addEdge(u,v)
        return g


    def __init__(self, undirected = False):
        self.vertices = []
        self.vertexMap = {}
        self.undirected = undirected
    def getNumVertices(self):
        return len(self.vertices)
    def addVertex(self,vname):
        id = self.getNumVertices()
        vertex = Vertex(vname)
        vertex.id = id
        self.vertexMap[vertex.getName()]=vertex.id
        self.vertices.append(vertex)
        return self
    def __getVertex(self,idx):
        return self.vertices[idx]
    def __getVertexByName(self,name):
        return self.__getVertex(self.vertexMap[name])
    def addEdge(self,uname,vname):
        self.__getVertexByName(uname).addEdge(self.__getVertexByName(vname).id)
        if(self.undirected):
            # add a reverse edge as well
            self.__getVertexByName(vname).addEdge(self.__getVertexByName(uname).id)
    def getVertices(self):
        return list(map(lambda x: x.name,self.vertices))
    def getNumEdgesFrom(self,vname):
        return self.__getVertexByName(vname).getNumEdges()
    def DFS(self):

        """
        enum class color
        defines three enums 
        used as vertex states
        as it is traversed DFS
        """
        class Color(enum.Enum):
            WHITE = 1
            GRAY = 2
            BLACK = 3


        num_vertices = self.getNumVertices()

        # used to maintain state for each vertex
        # each vertex can be either 
        # unvisited, discovered, finished 
        # these states are represented by colors
        # WHITE, GRAY and BLACK respectively
        color = [Color.WHITE] * num_vertices
    
        #
        #  Matrix used to store edge types
        #
        edge_matrix = []
        for i in range(0,num_vertices):
            p = [0]*num_vertices
            edge_matrix.append(p)

        # predecessor array. After DFS pi[u] points to the vertex from
        # which 'u' was first discovered
        # it can be used to build dfs-search-tree
        pi = [None] * num_vertices

        # d[u] contains the time when vertex u is visited
        d = [0] * num_vertices

        # f[u] contains the time when vertex u is finished 
        f = [0] * num_vertices

        # initialize color and pi
        for u in range(0,num_vertices):
            color[u] = Color.WHITE
            pi[u] = None
        
        time = 0


        # DFS_VISIT sub routine used by
        # DFS 
        def DFS_VISIT(u):
            color[u] = Color.GRAY
            nonlocal time
            time = time + 1
            d[u] = time
            vertex_u = self.__getVertex(u)
            for edge_idx in range(0,vertex_u.getNumEdges()):
                v = vertex_u.getEdge(edge_idx)

                if edge_matrix[u][v] == 0 and ((not self.undirected) or edge_matrix[v][u] == 0) and color[v] == Color.WHITE:
                    edge_matrix[u][v] = EdgeType.TREE_EDGE              
                elif edge_matrix[u][v] == 0 and ((not self.undirected) or edge_matrix[v][u] == 0) and color[v] == Color.GRAY:
                    edge_matrix[u][v] = EdgeType.BACK_EDGE
                elif edge_matrix[u][v] == 0 and ((not self.undirected) or edge_matrix[v][u] == 0) and d[u] < d[v]:
                    edge_matrix[u][v] = EdgeType.FORWARD_EDGE
                elif edge_matrix[u][v] == 0 and ((not self.undirected) or edge_matrix[v][u] == 0) and d[u] > d[v]:
                    edge_matrix[u][v] = EdgeType.CROSS_EDGE

                # first time discovering v
                if color[v] == Color.WHITE:            
                    pi[v] = u
                    DFS_VISIT(v)

            # vertex u is finished
            color[u] = Color.BLACK
            time = time + 1
            f[u] = time

        DFSResult = namedtuple("DFSResult",["pi","d","f","edge_type"])


        for u in range(0, num_vertices):
            if color[u] == Color.WHITE:
                DFS_VISIT(u)
    
        return DFSResult(pi,d,f,edge_type=edge_matrix)    



class EdgeType(enum.Enum):
    TREE_EDGE = 1
    BACK_EDGE = 2
    FORWARD_EDGE = 3
    CROSS_EDGE = 4




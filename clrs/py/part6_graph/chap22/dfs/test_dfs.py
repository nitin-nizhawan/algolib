import unittest
from part6_graph.chap22.dfs import dfs

class TestDFS(unittest.TestCase):

    # simple graph test with two vertices 0 and 1 and one edge
    # (0) ---- (1)
    def test_simple_graph(self):
        g = dfs.AdjGraph()
        va = dfs.Vertex("a")
        vb = dfs.Vertex("b")
        g.addVertex(va)
        g.addVertex(vb)
        va.addEdge(1)
        self.assertEquals(2,g.getNumVertices(),"should be eq")
        self.assertEquals(1,g.getVertex(0).getNumEdges(),"num edges should be 1")

    # builds graph as represented in following 6x6  matrix    
    #     u v w x y z
    #     0 1 2 3 4 5
    # u 0 0 1 0 1 0 0 
    # v 1 0 0 0 0 1 0 
    # w 2 0 0 0 0 1 1 
    # x 3 0 1 0 0 0 0 
    # y 4 0 0 0 1 0 0
    # z 5 0 0 0 0 0 1
    def createCRLSGraph(self):
        g = dfs.AdjGraph()
        g.addVertex(dfs.Vertex("u")) 
        g.addVertex(dfs.Vertex("v"))
        g.addVertex(dfs.Vertex("w"))
        g.addVertex(dfs.Vertex("x"))
        g.addVertex(dfs.Vertex("y"))
        g.addVertex(dfs.Vertex("z"))

        # add edges
        g.getVertex(0).addEdge(1).addEdge(3)
        g.getVertex(1).addEdge(4)
        g.getVertex(2).addEdge(4).addEdge(5)
        g.getVertex(3).addEdge(1)
        g.getVertex(4).addEdge(3)
        g.getVertex(5).addEdge(5)
        return g

    def test_clrs_graph(self):
        g = self.createCRLSGraph()
        self.assertEquals(6,g.getNumVertices(),"should have 6 vertices")
        numEdges = 0
        for i in range(0,g.getNumVertices()):
            numEdges = numEdges + g.getVertex(i).getNumEdges()
        self.assertEquals(8, numEdges,"total edges should be 8")

    def test_dfs(self):
        g = self.createCRLSGraph()
        result = dfs.DFS(g)
        print(result.pi)
        print(result.d)
        print(result.f)
        self.assertEquals(6,len(result.pi),"pre decessor should be 6")

    def test_edge_types(self):
        g = self.createCRLSGraph()
        num_vertices = g.getNumVertices()
        result = dfs.DFS(g)
        edge_matrix = result.edge_type
        for u in range(0,num_vertices):
            for v in range(0, num_vertices):
                uname = g.getVertex(u).name
                vname = g.getVertex(v).name
                if edge_matrix[u][v] != 0:
                    print("edge ("+uname+","+vname+") is ",edge_matrix[u][v]) 

if __name__ == "__main__":
    unittest.main()

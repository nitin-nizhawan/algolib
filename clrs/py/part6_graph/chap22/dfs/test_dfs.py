import unittest
from part6_graph.chap22.dfs import dfs

"""class to test dfs
"""
class TestDFS(unittest.TestCase):

    # simple graph test with two vertices 0 and 1 and one edge
    # (0) ---- (1)
    def test_simple_graph(self):
        g = dfs.AdjGraph()
        g.addVertex("a")
        g.addVertex("b")
        g.addEdge("a","b")
        self.assertEqual(2,g.getNumVertices(),"should be eq")
        self.assertEqual(1,g.getNumEdgesFrom("a"),"num edges should be 1")

    # builds graph as represented in following 6x6  matrix    
    #     u v w x y z
    #     0 1 2 3 4 5
    # u 0 0 1 0 1 0 0 
    # v 1 0 0 0 0 1 0 
    # w 2 0 0 0 0 1 1 
    # x 3 0 1 0 0 0 0 
    # y 4 0 0 0 1 0 0
    # z 5 0 0 0 0 0 1
    def createCRLSGraph(self,undirected = False):
        g = dfs.AdjGraph(undirected)
        g.addVertex("u") 
        g.addVertex("v")
        g.addVertex("w")
        g.addVertex("x")
        g.addVertex("y")
        g.addVertex("z")

        # add edges
        g.addEdge("u","v")
        g.addEdge("u","x")
        
        g.addEdge("v","y")

        g.addEdge("w","y")
        g.addEdge("w","z")

        g.addEdge("x","v")

        g.addEdge("y","x")

        g.addEdge("z","z")
        return g

    def test_clrs_graph(self):
        g = self.createCRLSGraph()
        self.assertEqual(6,g.getNumVertices(),"should have 6 vertices")
        numEdges = 0
        for vertex in g.getVertices():
            numEdges = numEdges + g.getNumEdgesFrom(vertex)
        self.assertEqual(8, numEdges,"total edges should be 8")

    def test_dfs(self):
        g = self.createCRLSGraph()
        result = g.DFS()
        print(result.pi)
        print(result.d)
        print(result.f)
        self.assertEqual(6,len(result.pi),"pre decessor should be 6")

    """there are 4 tree edges in graph and there are n vertices
    dfs finds a forrest with two dfs trees
    1 tree having 4 vertices and 3 tree edges and 1 tree having 2 vertices and 1 tree edge
    """
    def test_edge_types(self):
        g = self.createCRLSGraph()
        num_vertices = g.getNumVertices()
        result = g.DFS()
        edge_matrix = result.edge_type

        # following edges are tree edges
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[0][1])
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[1][4])
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[2][5])
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[4][3])

        # following two are backedges
        self.assertEqual(dfs.EdgeType.BACK_EDGE, edge_matrix[3][1])
        self.assertEqual(dfs.EdgeType.BACK_EDGE, edge_matrix[5][5])

        # following is forward edges
        self.assertEqual(dfs.EdgeType.FORWARD_EDGE, edge_matrix[0][3])

        # 1 cross edge
        self.assertEqual(dfs.EdgeType.CROSS_EDGE, edge_matrix[2][4])
    
    def test_edge_types_undirected(self):
        # create undirected graph
        g = self.createCRLSGraph(True)
        num_vertices = g.getNumVertices()
        result = g.DFS()
        edge_matrix = result.edge_type
        # following edges are tree edges
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[0][1])
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[1][4])
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[2][5])
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[4][2])
        self.assertEqual(dfs.EdgeType.TREE_EDGE, edge_matrix[4][3])

        # following three are backedges
        self.assertEqual(dfs.EdgeType.BACK_EDGE, edge_matrix[3][0])
        self.assertEqual(dfs.EdgeType.BACK_EDGE, edge_matrix[3][1])
        self.assertEqual(dfs.EdgeType.BACK_EDGE, edge_matrix[5][5])


if __name__ == "__main__":
    unittest.main()

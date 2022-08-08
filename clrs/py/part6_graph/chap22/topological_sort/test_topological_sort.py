import unittest
from part6_graph.chap22.dfs import dfs
from part6_graph.chap22.topological_sort import topological_sort

class TestTopologicalSort(unittest.TestCase):

    def createCRLSGraph(self):
        g = dfs.AdjGraph.CreateGraphFromDict(
        {
            "undershorts":["pants","shoes"],
            "pants":["belt","shoes"],
            "belt":["jacket"],
            "jacket":[],
            "tie":["jacket"],
            "shirt":["belt","tie"],
            "shoes":[],
            "socks":["shoes"],
            "watch":[],
        }
        )

        return g

    def test_ts_graph(self):
        g = self.createCRLSGraph()
        topo_order = topological_sort.topological_sort(g)

        result = list(map(lambda x: x.name,topo_order))
        
        self.assertEquals("jacket",result[len(result)-1],"jacket should be worn last")
        self.assertGreater(result.index("belt"),result.index("undershorts"),"belt should be worn after undershorts")


if __name__ == "__main__":
    unittest.main()

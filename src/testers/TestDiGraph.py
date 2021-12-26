import unittest
from Loc_Node_Edge import Location, Node
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_node(self):
        g = DiGraph()
        g.add_node(0, (1, 2, 3))
        g.add_node(1, (2, 3, 4))
        self.assertTrue(g.key_nodes.get(0) is not g.key_nodes.get(1))

    def test_edge(self):
        g = DiGraph()
        g.add_node(0, (1, 2, 3))
        g.add_node(1, (2, 3, 4))
        node = g.key_nodes.get(0)

if __name__ == '__main__':
    unittest.main()

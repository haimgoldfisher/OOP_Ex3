import unittest
from GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)

    def test_load_save(self):
        graph = GraphAlgo()
        graph.load_from_json("data/A0.json")
        graph.save_to_json("A0_save")

if __name__ == '__main__':
    unittest.main()

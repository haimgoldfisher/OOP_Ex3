import math
import unittest
from GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):

    def test_load_save(self):
        graph = GraphAlgo()
        graph.load_from_json("../data/A0.json")
        graph.save_to_json("A0_save")
        graph1, graph2 = GraphAlgo(), GraphAlgo()
        graph1.load_from_json("../data/A0.json")
        graph2.load_from_json("A0_save.json")
        self.assertEqual(graph1.get_graph().get_all_v().keys(), graph2.get_graph().get_all_v().keys()) # nodes
        self.assertEqual(graph1.get_graph().edge_counter, graph2.get_graph().edge_counter) # edges

    def test_isConnected(self):
        g_A0, g_A1, g_A2, g_A3, g_A4, g_A5, g_T0 = GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo()
        g_A0.load_from_json("../data/A0.json"), g_A1.load_from_json("../data/A1.json"),
        g_A2.load_from_json("../data/A2.json"), g_A3.load_from_json("../data/A3.json"),
        g_A4.load_from_json("../data/A4.json"), g_A5.load_from_json("../data/A5.json"),
        g_T0.load_from_json("../data/T0.json")
        self.assertTrue(g_A0.isConnected())
        self.assertTrue(g_A1.isConnected())
        self.assertTrue(g_A2.isConnected())
        self.assertTrue(g_A3.isConnected())
        self.assertTrue(g_A4.isConnected())
        self.assertTrue(g_A5.isConnected())
        self.assertFalse(g_T0.isConnected()) # should return false

    def test_dijkstra(self):
        g_A0, g_A1, g_A2, g_T0 = GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo()
        g_A0.load_from_json("../data/A0.json"), g_A1.load_from_json("../data/A1.json"),
        g_A2.load_from_json("../data/A2.json"),
        g_T0.load_from_json("../data/T0.json")
        self.assertEqual(g_A0.dijkstra(3), ((7.286831393469998, 3), {0: 4.702068088352025, 1: 2.8136021362086723, 2: 1.0980094622804095, 3: 0, 4: 1.4301580756736283, 5: 3.374437071805205, 6: 4.53509972816613, 7: 5.931935744533007, 8: 7.286831393469998, 9: 7.252817483848961, 10: 6.164094904860583}, {2: 3, 4: 3, 1: 2, 5: 4, 0: 1, 6: 5, 7: 6, 10: 0, 8: 7, 9: 10}))
        self.assertEqual(g_A1.dijkstra(10), ((10.420668700653765, 10), {0: 10.420668700653765, 1: 9.853258486782712, 2: 8.27475938565515, 3: 9.337919899925136, 4: 9.509376377473123, 5: 7.9237850863068875, 6: 6.427354662694587, 7: 4.848746472647887, 8: 3.5670093815141426, 9: 1.5815006562559664, 10: 0, 11: 1.4962204797190428, 12: 3.4278264711104334, 13: 4.976237441396691, 14: 5.987309428481768, 15: 7.106259784402749, 16: 8.97886693551901}, {9: 10, 11: 10, 12: 11, 8: 9, 13: 12, 7: 8, 6: 7, 14: 13, 15: 14, 2: 6, 5: 6, 16: 15, 4: 5, 1: 2, 3: 2, 0: 16}))
        self.assertEqual(g_A2.dijkstra(27), ((10.824883531818315, 27), {0: 6.333439881707073, 1: 4.469872819320036, 2: 4.293557694490976, 3: 5.356718208760963, 4: 5.528174686308948, 5: 3.9425833951427136, 6: 2.446152971530413, 7: 0.8675447814837128, 8: 2.2392800799542782, 9: 3.772135401935012, 10: 5.058309320524671, 11: 6.554529800243714, 12: 8.486135791635103, 13: 9.81381154473324, 14: 10.824883531818315, 15: 9.213080850434153, 16: 7.645311517949043, 17: 10.775028039868978, 18: 9.206922444440037, 19: 8.666313267305343, 20: 7.787559662832152, 21: 6.599044841057438, 22: 5.824009413133958, 23: 4.8072037404443915, 24: 4.307103298652044, 25: 3.2644295190375443, 26: 3.4432674616935874, 27: 0, 28: 5.0455447647369995, 29: 6.341677388533064, 30: 8.812810536634924}, {7: 27, 6: 7, 8: 7, 9: 8, 25: 8, 26: 8, 2: 6, 5: 6, 24: 25, 1: 26, 23: 9, 10: 9, 4: 5, 28: 5, 3: 2, 0: 1, 22: 23, 29: 28, 11: 10, 21: 22, 16: 0, 20: 11, 12: 11, 15: 16, 18: 20, 19: 20, 30: 20, 13: 30, 17: 18, 14: 13}))

    def test_center(self):
        g_A0, g_A1, g_A2, g_A3, g_A4, g_A5, g_T0 = GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo()
        g_A0.load_from_json("../data/A0.json"), g_A1.load_from_json("../data/A1.json"),
        g_A2.load_from_json("../data/A2.json"), g_A3.load_from_json("../data/A3.json"),
        g_A4.load_from_json("../data/A4.json"), g_A5.load_from_json("../data/A5.json"),
        g_T0.load_from_json("../data/T0.json")
        self.assertEqual(g_A0.centerPoint(), (7, 6.806805834715163))
        self.assertEqual(g_A1.centerPoint(), (8, 9.925289024973141))
        self.assertEqual(g_A2.centerPoint(), (0, 7.819910602212574))
        self.assertEqual(g_A3.centerPoint(), (2, 8.182236568942237))
        self.assertEqual(g_A4.centerPoint(), (6, 8.071366078651435))
        self.assertEqual(g_A5.centerPoint(), (40, 9.291743173960954))
        self.assertEqual(g_T0.centerPoint(), (None, math.inf))

    def test_shortest_path(self):
        g_A0, g_A1, g_A2, g_A3, g_A4, g_A5, g_T0 = GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo()
        g_A0.load_from_json("../data/A0.json"), g_A1.load_from_json("../data/A1.json"),
        g_A2.load_from_json("../data/A2.json"), g_A3.load_from_json("../data/A3.json"),
        g_T0.load_from_json("../data/T0.json")
        self.assertEqual(g_A0.shortest_path(0, 10), (1.4620268165085584, [0, 10]))
        self.assertEqual(g_A1.shortest_path(5, 1), (5.160215750118257, [5, 6, 2, 1]))
        self.assertEqual(g_A2.shortest_path(4, 17), (11.956745294737042, [4, 3, 2, 1, 0, 16, 15, 14, 17]))
        self.assertEqual(g_A3.shortest_path(21, 6), (5.780771231445064, [21, 0, 1, 2, 6]))

    def test_TSP(self):
        g_A0, g_A1, g_A2, g_A3, g_A4, g_A5, g_T0 = GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo(), GraphAlgo()
        g_A0.load_from_json("../data/A0.json"), g_A1.load_from_json("../data/A1.json"),
        g_A2.load_from_json("../data/A2.json"), g_A3.load_from_json("../data/A3.json"),
        g_A4.load_from_json("../data/A4.json"),
        g_T0.load_from_json("../data/T0.json")
        self.assertEqual(g_A0.TSP([0, 5, 4, 9]), ([0, 10, 9, 8, 7, 6, 5, 4], 9.800910116222662))
        self.assertEqual(g_A1.TSP([11, 8, 0, 15]), ([8, 9, 10, 11, 12, 13, 14, 15, 16, 0], 13.239697941224158))
        self.assertEqual(g_A2.TSP([30, 6, 13, 29]), ([29, 28, 5, 6, 7, 8, 9, 10, 11, 20, 30, 13], 13.945296299049303))
        self.assertEqual(g_A3.TSP([21, 44, 2, 11]), ([11, 10, 9, 23, 22, 21, 0, 1, 2, 6, 7, 44], 13.73082980361677))
        self.assertEqual(g_A4.TSP([0, 1, 2, 3, 4, 5, 6, 10]), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15.062841839696361))

    def test_init_random(self):
        g = GraphAlgo()
        g.init_random(1)
        self.assertEqual(g.graph.get_all_v().keys().__len__(), 10)
        self.assertEqual(g.graph.edge_counter, 20) # cant be at deg 20, no enough nodes
        self.assertTrue(g.isConnected())
        g.init_random(2)
        self.assertEqual(g.graph.get_all_v().keys().__len__(), 100)
        self.assertEqual(g.graph.edge_counter, 1000) # deg 20 - 10 in 10 out
        self.assertTrue(g.isConnected())
        g.init_random(3)
        self.assertEqual(g.graph.get_all_v().keys().__len__(), 1000)
        self.assertEqual(g.graph.edge_counter, 10000) # deg 20 - 10 in 10 out
        self.assertTrue(g.isConnected())

if __name__ == '__main__':
    unittest.main()

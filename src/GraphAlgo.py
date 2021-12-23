import copy
import math
import queue
from queue import PriorityQueue
from types import SimpleNamespace
from typing import List
import json
import os
import GraphInterface
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from Loc_Node_Edge import Node, Location


class GraphAlgo(GraphAlgoInterface):
    def __init__(self) -> None:
        self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as json_file:
                jobj = json.load(json_file)
                edges = jobj.get("Edges")
                nodes = jobj.get("Nodes")
                for d in nodes:
                    node_id = d.get("id")
                    pos = d.get("pos")
                    if pos is not None:
                        pos = pos.split(",")
                        new_loc = Location(pos[0], pos[1], pos[2])
                        self.graph.add_node(node_id, new_loc.pos)
                    else:
                        self.graph.add_node(node_id, None)

                for d in edges:
                    src = d["src"]
                    w = d["w"]
                    dest = d["dest"]
                    self.graph.add_edge(src, dest, w)
                return True
        except FileExistsError as err:
            print(err)
            return False

    #    root_path = os.path.dirname(os.path.abspath(__file__))

    #    with open(root_path + '/students.json', 'r') as file:
    #       list_of_stud_dict = json.load(file)['students']
    #       list_of_stud = [Student(**s) for s in list_of_stud_dict]

    def save_to_json(self, file_name: str) -> bool:
        try:
            json_obj = json.dumps(self.graph)
            return True
        except IOError as err:
            print(err)
            return False

    def reverse(self, graph) -> DiGraph:
        ans = copy.deepcopy(graph)
        new_edges_list = list()
        for nd in ans.key_nodes.values():
            for edge_data in nd.child_weight.items():
                x = (edge_data[0], nd.key, edge_data[1])
                new_edges_list.append(x)
            nd.child_weight.clear()
            nd.parent_weight.clear()
        ans.edge_counter = 0
        for edge_data in new_edges_list:
            ans.add_edge(edge_data[0], edge_data[1], edge_data[2])
        return ans

    def isConnected(self) -> bool:
        keys = list(self.graph.key_nodes.keys())
        key = keys[0]
        visited = self.graph.my_dfs(key)
        if visited != self.graph.v_size():
            return False
        g_copy = copy.deepcopy(self.graph)
        reversed_g = self.reverse(g_copy)
        visited = reversed_g.my_dfs(key)
        if visited != self.graph.v_size():
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        if id1 == id2:
            path.append(id1)
            return 0, path
        previous = dict()
        distances = dict()
        visited = dict()
        keys = self.graph.key_nodes.copy()
        pq = queue.PriorityQueue()
        for key in keys.keys():
            distances[key] = math.inf
        distances[id1] = 0
        pq.put((0, id1))
        while visited.__len__() != keys.__len__():
            if pq.qsize() == 0:
                break
            curr_key = pq.get()[1]
            if visited.get(curr_key) is not None:
                continue
            visited[curr_key] = True
            curr_nd = keys.get(curr_key)
            for edge in curr_nd.child_weight.items():
                curr_dest = edge[0]
                weight = edge[1]
                if visited.get(curr_dest) is not None:
                    continue
                curr_weight = distances.get(curr_dest)
                new_weight = distances.get(curr_key) + weight
                if new_weight < curr_weight:
                    distances[curr_dest] = new_weight
                    previous[curr_dest] = curr_key
                pq.put((distances.get(curr_dest), curr_dest))
        if distances.get(id2) == math.inf:
            return -1, None
        curr = id2
        while curr != id1:
            path.insert(0, curr)
            curr = previous.get(curr)
        dist = distances.get(id2)
        return dist, path  # distance

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        if not self.isConnected():
            return None
        e = dict()
        lst = []
        for src in self.graph.key_nodes.keys():
            curr_maximum_src = self.dijkstra(src)
            lst.append(curr_maximum_src)
        max_min = min(lst)
        max_min_dist = max_min[0]
        key = max_min[1]
        nd = self.graph.key_nodes.get(key)
        return key, max_min_dist

    def dijkstra(self, src):
        distances = dict()
        visited = dict()
        keys = self.graph.key_nodes.copy()
        pq = queue.PriorityQueue()
        for key in keys.keys():
            distances[key] = math.inf
        distances[src] = 0
        pq.put((0, src))
        while visited.__len__() != keys.__len__():
            if pq.qsize() == 0:
                break
            curr_key = pq.get()[1]
            if visited.get(curr_key) is not None:
                continue
            visited[curr_key] = True
            curr_nd = keys.get(curr_key)
            for edge in curr_nd.child_weight.items():
                curr_dest = edge[0]
                weight = edge[1]
                if visited.get(curr_dest) is not None:
                    continue
                curr_weight = distances.get(curr_dest)
                new_weight = distances.get(curr_key) + weight
                if new_weight < curr_weight:
                    distances[curr_dest] = new_weight
                pq.put((distances.get(curr_dest), curr_dest))
        maximum = -math.inf
        max_id = -1
        for key in keys.keys():
            if distances.get(key) > maximum and distances.get(key) != math.inf:
                maximum = distances.get(key)
                max_id = key
        ans = (maximum, src)
        return ans

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    g = GraphAlgo()
    g.load_from_json("../data/T0.json")
    print(g.graph)
    print(g.isConnected())
    print(g.centerPoint())

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
from Loc_Node_Edge import Node, Edge


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph) -> None:
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as json_file:
                self.graph.graph = json.load(
                    json_file, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
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

    def reverse(graph) -> DiGraph:
        ans = copy.deepcopy(graph)
        keys_list = list
        for key in ans.get_graph().key_edges.keys():
            keys_list.append(key)
        for i in enumerate(keys_list):
            key = keys_list[i]
            removed_edge = ans.remove_edge(key[0], key[1])
        for key in graph.key_edges.keys():
            edge = graph.key_edges.get(key[0], key[1])
            ans.connect(key[1], key[0], edge.weight)
        return ans

    def isConnected(self) -> bool:
        keys = list(self.graph.key_nodes.keys())
        key = keys[0]
        visited = self.graph.my_dfs(key)
        if visited != self.graph.v_size():
            return False
        g_copy = copy.deepcopy(self.graph)
        reversed_g = reverse(g_copy)
        visited = reversed_g.myDFS(key)
        if visited != self.graph.v_size():
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = list
        if id1 == id2:
            path.append(self.graph.key_nodes.get(id1))
            return 0, path
        previous, distances, visited, keys = dict, dict, dict, dict
        keys.update(self.graph.key_nodes.keys())
        pq = PriorityQueue
        for key in keys:
            distances.update(key, float('inf'))
        distances.update(id1, 0)
        pq.put(id1, 0)
        while len(visited) != len(keys):
            if pq.empty():
                break
            curr_key = pq.pop.get()
            if curr_key is id2:
                break
            if curr_key in visited:
                continue
            visited.update(curr_key)
            curr_node = self.graph.key_nodes.get(curr_key)
            for edge in curr_node.edges_to_children:
                curr_edge = edge
                curr_dest = curr_edge.dest
                if curr_dest in visited:
                    continue
                curr_weight = distances.get(curr_dest)
                new_weight = distances.get(curr_key) + curr_edge.weight
                if new_weight < curr_weight:
                    distances.update(curr_dest, new_weight)
                    previous.update(curr_dest, curr_key)
                pq.put(curr_dest, distances.get(curr_dest))

        if distances.get(id2) == float('inf'):
            return None
        curr = id2
        while curr != id1:
            curr_node = self.graph.key_nodes.get(curr)
            path.append(curr_node)
            curr = previous.get(curr)
        src_node = self.graph.key_nodes.get(id1)
        path.append(src_node)
        return path,  # distance

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        if self.isConnected is False:
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
        pq.add((0, src))
        while visited.__len__() != keys.__len__():
            if pq.not_empty():
                break
            curr_key = pq.get()
            if visited.get(curr_key) is not None:
                continue
            visited[curr_key] = True
            curr_nd = keys.get(curr_key)
            for edge in curr_nd.child_weight.items():
                curr_dest = edge[1]
                weight = edge[0]
                if visited.get(curr_dest) is not None:
                    continue
                curr_weight = distances.get(curr_dest)
                new_weight = distances.get(curr_key) + weight
                if new_weight < curr_weight:
                    distances[curr_dest] = new_weight
                pq.add((distances.get(curr_dest), curr_dest))
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

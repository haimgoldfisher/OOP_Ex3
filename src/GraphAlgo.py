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
                self.graph = json.load(
                    json_file, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
        except FileExistsError as err:
            print(err)

#    root_path = os.path.dirname(os.path.abspath(__file__))

#    with open(root_path + '/students.json', 'r') as file:
 #       list_of_stud_dict = json.load(file)['students']
 #       list_of_stud = [Student(**s) for s in list_of_stud_dict]

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass

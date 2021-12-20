from GraphInterface import GraphInterface
from Loc_Node_Edge import Location
from Loc_Node_Edge import Node
from Loc_Node_Edge import Edge


class DiGraph(GraphInterface):
    def __init__(self, key_nodes: dict, key_edges: dict, mc: int) -> None:
        self.key_nodes = key_nodes
        self.key_edges = key_edges
        self.mc = mc

    def v_size(self) -> int:
        return len(self.key_nodes)

    def e_size(self) -> int:
        return len(self.key_edges)

    def get_all_v(self) -> dict:
        return self.key_nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        pass

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.key_nodes.get(id1).edges_to_children

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        pass

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass

    def my_dfs(self, start: int) -> int:
        counter = 0
        key_visited = dict
        keys = dict
        keys.update(self.key_nodes.keys())
        for key in keys:
            key_visited.update(key, False)
        stack = [start]
        key_visited.update(start, True)
        counter = counter + 1
        while len(stack) is not 0:
            curr_id = stack.pop()
            curr_node = self.key_nodes.get(curr_id)
            for child_key in curr_node.children_keys:
                if key_visited.get(child_key) is not None and key_visited.get(child_key) is False:
                    stack.append(child_key)
                    key_visited.update(child_key, True)
                    counter = counter + 1
        return counter



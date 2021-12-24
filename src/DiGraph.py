import queue
import random

from GraphInterface import GraphInterface
from Loc_Node_Edge import Node, Location


class DiGraph(GraphInterface):
    # def __init__(self, key_nodes: dict, key_edges: dict, mc: int) -> None:
    #     self.key_nodes = key_nodes
    #     self.key_edges = key_edges
    #     self.graph = {"Nodes": self.key_nodes, "Edges": key_edges}
    #     self.mc = mc

    def __init__(self) -> None:
        self.key_nodes = dict()
        self.edge_counter = 0
        self.mc = 0

    def v_size(self) -> int:
        return len(self.key_nodes)

    def e_size(self) -> int:
        return self.edge_counter

    def get_all_v(self) -> dict:
        return self.key_nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.key_nodes.get(id1).parent_weight

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.key_nodes.get(id1).child_weight

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.key_nodes.get(id1) is None or self.key_nodes.get(id2) is None:
            return False
        nd1 = self.key_nodes.get(id1)
        nd2 = self.key_nodes.get(id2)
        nd1.child_weight[id2] = weight
        nd2.parent_weight[id1] = weight
        self.edge_counter += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.key_nodes.__contains__(node_id):
            return False
        if pos is None:
            x = 35 + random.random()
            y = 32 + random.random()
            z = 0
            new_pos = Location(x, y, z)
            new_nd = Node(node_id, new_pos.pos)
        else:
            new_nd = Node(node_id, pos)
        self.key_nodes[node_id] = new_nd
        return

    def remove_node(self, node_id: int) -> bool:
        if self.key_nodes.get(node_id) is None:
            return False
        nd = self.key_nodes.get(node_id)
        for curr_id in nd.parent_weight.keys():
            curr_nd = self.key_nodes.get(curr_id)
            curr_nd.child_weight.__delitem__(node_id)
            self.edge_counter -= 1
        for curr_id in nd.child_weight.keys():
            curr_nd = self.key_nodes.get(curr_id)
            curr_nd.parent_weight.__delitem__(node_id)
            self.edge_counter -= 1
        self.key_nodes.__delitem__(node_id)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.key_nodes.get(node_id1) is None or self.key_nodes.get(node_id2) is None:
            return False
        nd1 = self.key_nodes.get(node_id1)
        nd2 = self.key_nodes.get(node_id2)
        if nd1.child_weight.get(node_id2) is None or nd2.parent_weight.get(node_id1) is None:
            return False
        nd1.child_weight.__delitem__(node_id2)
        nd2.parent_weight.__delitem__(node_id1)
        self.edge_counter -= 1
        return True

    def my_dfs(self, start: int) -> int:
        counter = 0
        key_visited = dict()
        # keys = dict
        # keys.update(self.key_nodes.keys())
        for key in self.key_nodes.keys():
            key_visited[key] = False
        stack = [start]
        key_visited[start] = True
        counter = counter + 1
        while len(stack) != 0:
            curr_id = stack.pop()
            curr_node = self.key_nodes.get(curr_id)
            for child_key in curr_node.child_weight.keys():
                if key_visited.get(child_key) is not None and key_visited.get(child_key) is False:
                    stack.append(child_key)
                    key_visited[child_key] = True
                    counter = counter + 1
        return counter

    def __str__(self):
        return "Graph: |V|={} , |E|={}".format(self.key_nodes.__len__(), self.edge_counter)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    # g = DiGraph()  # creates an empty directed graph
    # for n in range(4):
    #     g.add_node(n)
    # g.add_edge(0, 1, 1)
    # g.add_edge(1, 0, 1.1)
    # g.add_edge(1, 2, 1.3)
    # g.add_edge(2, 3, 1.1)
    # g.add_edge(1, 3, 1.9)
    # g.remove_edge(1, 3)
    # g.add_edge(1, 3, 10)
    # print(g)  # prints the __repr__ (func output)
    # print(g.get_all_v())  # prints a dict with all the graph's vertices.
    # print(g.all_in_edges_of_node(1))
    # print(g.all_out_edges_of_node(1))
    # # g_algo = GraphAlgo(g)
    # # print(g_algo.shortest_path(0, 3))
    # # g_algo.plot_graph()
    #
    x = {1:"a" , 2:"b"}
    x.clear()
    print(x)
    # x = (1,2)
    # print(x[0])
    # for i in x.items():
    #     print(i[1])
    # pq = queue.PriorityQueue()
    # pq.put((2.5, 0))
    # pq.put((1.5, 1))
    # pq.put((4.5, 2))
    # pq.put((0.5, 3))
    # while(pq.not_empty):
    #     print(pq.get())
    print("as,cv,hd".split(","))

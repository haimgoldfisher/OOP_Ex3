import GraphInterface


class DiGraph(GraphInterface):
    def __init__(self, key_nodes: dict, key_edges: dict, mc: int) -> None:
        self.key_nodes = key_nodes
        self.key_edges = key_edges
        self.mc = mc

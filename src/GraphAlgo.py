import GraphAlgoInterface
import DiGraph


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph) -> None:
        self.graph = graph
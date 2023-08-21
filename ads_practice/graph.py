from __future__ import annotations
import json
from dataclasses import dataclass


@dataclass
class Edge:
    to: int
    weigth: int


class AdjacencyList:
    def __init__(self):
        self.graph: dict = {}

    def add_edge(self, origin, destination, weight):
        if origin not in self.graph:
            self.graph[origin] = []
        if destination not in self.graph:
            self.graph[destination] = []
        self.graph[origin].append(Edge(destination, weight))

    def is_connected(self, origin: int, destination: int) -> bool:
        if origin not in self.graph:
            return False
        edges = self.graph[origin]
        for edge in edges:
            if edge.to == destination:
                return True
        return False

    def get_edges(self, vertex: int) -> list[Edge]:
        if vertex not in self.graph:
            return []
        return self.graph[vertex]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

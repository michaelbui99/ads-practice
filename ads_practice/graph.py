from __future__ import annotations
import json
from dataclasses import dataclass
from ads_practice.queue import Queue


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


def bfs_adjmatrix(graph: list[list[int]], source: int, query: int) -> list[int]:
    seen = [False] * len(graph)
    prev = [-1] * len(graph)

    q = Queue()
    q.enqueue(source)
    seen[source] = True

    while not q.empty():
        curr = q.dequeue()
        if curr == query:
            break

        adjacent_vertices = graph[curr]
        for i in range(0, len(adjacent_vertices)):
            # No edge
            if adjacent_vertices[i] == 0:
                continue

            # Already visited
            if seen[i]:
                continue

            # Visit adjacent vertices
            seen[i] = True
            prev[i] = curr
            q.enqueue(i)

        seen[curr] = True

    curr = query
    res = []
    while prev[curr] != -1:
        res.append(curr)
        curr = prev[curr]

    if len(res) > 0:
        res.reverse()
        res = [source] + res
        return res

    return []

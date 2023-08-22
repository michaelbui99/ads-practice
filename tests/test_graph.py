from ads_practice.graph import AdjacencyList, bfs_adjmatrix


def test_adjlist_direction():
    graph = AdjacencyList()
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 3)

    assert graph.is_connected(1, 2) == True
    assert graph.is_connected(2, 1) == False
    assert graph.is_connected(1, 3) == True
    assert graph.is_connected(3, 1) == False
    assert graph.is_connected(2, 3) == False


def test_bfs_adjmatrix():
    graph = [
        [0, 3, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 5, 0, 2, 0],
        [0, 0, 18, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1],
    ]

    assert bfs_adjmatrix(graph, 0, 6) == [0, 1, 4, 5, 6]
    assert bfs_adjmatrix(graph, 6, 0) == []

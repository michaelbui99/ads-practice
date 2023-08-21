from ads_practice.graph import AdjacencyList


def test_adjlist_direction():
    graph = AdjacencyList()
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 3)

    assert graph.is_connected(1, 2) == True
    assert graph.is_connected(2, 1) == False
    assert graph.is_connected(1, 3) == True
    assert graph.is_connected(3, 1) == False
    assert graph.is_connected(2, 3) == False

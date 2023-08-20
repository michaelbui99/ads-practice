from ads_practice.minheap import MinHeap


def test():
    heap = MinHeap()

    heap.insert(5)
    heap.insert(3)
    heap.insert(69)
    heap.insert(420)
    heap.insert(4)
    heap.insert(1)
    heap.insert(8)
    heap.insert(7)

    assert len(heap) == 8
    assert heap.poll() == 1
    assert heap.poll() == 3
    assert heap.poll() == 4
    assert heap.poll() == 5
    assert len(heap) == 4
    assert heap.poll() == 7
    assert heap.poll() == 8
    assert heap.poll() == 69
    assert heap.poll() == 420
    assert len(heap) == 0

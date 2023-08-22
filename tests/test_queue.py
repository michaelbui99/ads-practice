from ads_practice.queue import Queue


def test():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)

    assert len(q) == 5
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert len(q) == 3
    assert q.dequeue() == 3
    assert q.dequeue() == 5
    assert q.dequeue() == 7
    assert len(q) == 0
    assert q.empty() == True

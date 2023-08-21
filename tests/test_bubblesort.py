from ads_practice.bubblesort import bubblesort


def test():
    xs = [9, 3, 7, 4, 69, 420, 42]
    bubblesort(xs)
    assert xs == [3, 4, 7, 9, 42, 69, 420]

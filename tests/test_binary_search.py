from ads_practice.binary_search import binary_search


def test():
    xs = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert (binary_search(xs, 69)) == True
    assert (binary_search(xs, 1336)) == False
    assert (binary_search(xs, 69420)) == True
    assert (binary_search(xs, 69421)) == False
    assert (binary_search(xs, 1)) == True
    assert (binary_search(xs, 0)) == False

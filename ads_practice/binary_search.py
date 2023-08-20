import math


def binary_search(xs: list[int], query: int) -> bool:
    low = 0
    high = len(xs)

    while low < high:
        mid = math.floor(low + (high - low) / 2)
        val = xs[mid]

        if val == query:
            return True

        if query < val:
            high = mid
        else:
            low = mid + 1

    return False

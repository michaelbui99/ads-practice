from typing import TypeVar

T = TypeVar("T")


def bubblesort(xs: list[T]):
    for i in range(0, len(xs)):
        for j in range(i, len(xs) - 1 - i):
            if xs[j] > xs[j + 1]:
                temp = xs[j]
                xs[j] = xs[j + 1]
                xs[j + 1] = temp

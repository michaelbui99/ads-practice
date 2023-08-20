import math


class MinHeap:
    def __init__(self):
        self.size: int = 0
        self.items: list[int] = []

    def __len__(self):
        return self.size

    def insert(self, item: int) -> None:
        self.items.append(item)
        self.size += 1
        self._heapify_up()

    def poll(self) -> int:
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self._heapify_down()
        if self.size == 0:
            self.items = []

        return item

    def _parent(self, child: int) -> int:
        return math.floor((child - 1) / 2)

    def _left_child(self, parent: int) -> int:
        return 2 * parent + 1

    def _right_child(self, parent: int) -> int:
        return 2 * parent + 2

    def _heapify_up(self):
        curr = self.size - 1
        while self._has_parent(curr):
            parent_val = self.items[self._parent(curr)]
            curr_val = self.items[curr]
            if parent_val < curr_val:
                break
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def _heapify_down(self):
        curr = 0
        while self._has_left_child(curr):
            smaller_child = self._left_child(curr)
            if (
                self._has_right_child(curr)
                and self.items[self._right_child(curr)] < self.items[smaller_child]
            ):
                smaller_child = self._right_child(curr)

            if self.items[curr] < self.items[smaller_child]:
                break

            self._swap(curr, smaller_child)
            curr = smaller_child

    def _swap(self, idx1: int, idx2: int) -> None:
        temp = self.items[idx1]
        self.items[idx1] = self.items[idx2]
        self.items[idx2] = temp

    def _has_parent(self, idx: int) -> bool:
        return self._parent(idx) >= 0

    def _has_left_child(self, idx: int) -> bool:
        return self._left_child(idx) < self.size

    def _has_right_child(self, idx: int) -> bool:
        return self._right_child(idx) < self.size

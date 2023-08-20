from __future__ import annotations
from dataclasses import dataclass
from typing import TypeVar, Callable

T = TypeVar("T")


class Maybe:
    def __init__(self, val: T, has_value: bool):
        self.val = val
        self.has_value = has_value

    @staticmethod
    def of(val: T):
        if val is None:
            return Maybe.empty()
        return Maybe(val, True)

    @staticmethod
    def empty():
        return Maybe(None, False)

    def unwrap(self) -> T:
        """
        Unsafe operation. Force unwrapping of inner value.
        """
        if not self.has_value:
            raise "Unwrapped no value"
        return self.val

    def or_else_get(self, factory: Callable[[], T]) -> T:
        """
        Return inner value, if value is present. If value is not present, then return value produced by the lambda passed to this method.
        """
        return self.val if self.has_value else factory()


@dataclass
class Node:
    val: T
    next: Node


class Stack:
    def __init__(self):
        self.size: int = 0
        self._items: list[T] = []
        self._head = None

    def push(self, item: T) -> None:
        self.size += 1
        if self._head is None:
            self._head = Node(item, None)
            return

        new_head = Node(item, self._head)
        self._head = new_head

    def pop(self) -> Maybe[T]:
        item = Maybe.empty()
        if self._head is not None:
            item = Maybe.of(self._head.val)
            self.size -= 1

        self._head = self._head.next if self._head is not None else None
        return item

    def peek(self) -> Maybe[T]:
        item = Maybe.empty()
        if self._head is not None:
            item = Maybe.of(self._head.val)
        return item

    def empty(self) -> bool:
        return self.size == 0

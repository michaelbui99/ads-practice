from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class Node:
    val: T
    next: Node


class Queue:
    def __init__(self):
        self.head: Node[T] = None
        self.tail: Node[T] = None
        self.length = 0

    def __len__(self):
        return self.length

    def peek(self) -> T:
        if self.length == 0:
            return None
        return self.head.val

    def enqueue(self, item: T) -> None:
        self.length += 1
        new_node = Node(item, None)

        if self.tail is None:
            self.tail = self.head = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self) -> T:
        if self.length == 0:
            return None

        self.length -= 1
        node = self.head
        self.head = self.head.next
        node.next = None

        if self.length == 0:
            self.head = self.tail = None

        return node.val

    def empty(self) -> bool:
        return len(self) == 0

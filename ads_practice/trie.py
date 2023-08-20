from __future__ import annotations
import string
import json
from typing import TypeVar


class TrieNode:
    def __init__(self, val: chr, is_word: bool):
        self.val: chr = val
        self.is_word: bool = is_word
        self.children: dict = {}

    @staticmethod
    def create_head_node() -> TrieNode:
        node = TrieNode("", False)
        alphabet = list(string.ascii_lowercase)
        for letter in alphabet:
            node.children[letter] = TrieNode.create_node(letter)
        return node

    @staticmethod
    def create_word_node(val: chr) -> TrieNode:
        return TrieNode(val, True)

    @staticmethod
    def create_node(val: chr) -> TrieNode:
        return TrieNode(val, False)

    def get_child(self, val: chr) -> TrieNode:
        if val not in self.children:
            return None

        return self.children[val]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

    def has_child(self, val: chr) -> bool:
        return self.get_child(val) != None


class Trie:
    def __init__(self):
        self._head = TrieNode.create_head_node()

    def insert(self, item: str) -> None:
        curr = self._head.get_child(item[0])
        i = 0
        item = item[1 : len(item)]
        for char in list(item):
            child = curr.get_child(char)
            if child is not None:
                curr = child
            else:
                node = (
                    TrieNode.create_node(char)
                    if i != len(item) - 1
                    else TrieNode.create_word_node(char)
                )
                curr.children[char] = node
                curr = node
            i += 1

    def _delete(self, curr: TrieNode, item: str, idx: int) -> None:
        if curr is None:
            return

        if idx == len(item) - 1:
            if curr.is_word:
                curr.is_word = False
            return

        self._delete(curr.get_child(item[idx + 1]), item, idx + 1)

    def delete(self, item: str) -> None:
        head = self._head.get_child(item[0])
        self._delete(head, item, 0)

    def _find(
        self,
        curr: TrieNode,
        partial: str,
        partial_idx: int,
        path: str,
        result: list[str],
    ) -> None:
        if curr is None:
            return

        path += curr.val

        if curr.is_word:
            result.append(path)

        new_idx = partial_idx + 1
        if new_idx > len(partial) - 1:
            for child in curr.children:
                self._find(curr.children[child], partial, new_idx, path, result)
        else:
            self._find(curr.get_child(partial[new_idx]), partial, new_idx, path, result)

    def find(self, partial: str) -> list[str]:
        res = []
        self._find(self._head.get_child(partial[0]), partial, 0, "", res)
        return res

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)

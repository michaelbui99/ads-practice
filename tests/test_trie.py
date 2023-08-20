from ads_practice.trie import Trie


def test():
    trie = Trie()
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("foolproof")
    trie.insert("bar")

    trie.delete("fool")
    assert "foo" in trie.find("fo")
    assert "foolish" in trie.find("fo")
    assert "fool" not in trie.find("fo")

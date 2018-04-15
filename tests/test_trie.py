
from unittest import TestCase

from data_structures.trees.trie import Trie


class TestTrie(TestCase):

    def test_insert(self):
        word = "apple"
        trie = Trie()
        trie.insert(word)
        assert trie.search(word)
        assert not trie.search("a")
        assert trie.prefix_search("a")
        assert not trie.search("ap")
        assert trie.prefix_search("ap")
        assert not trie.search("app")
        assert trie.prefix_search("app")
        assert not trie.search("appl")

    def test_bulk_insert(self):
        words = ("hello", "hi", "z")
        trie = Trie()
        trie.bulk_insert(words)
        for word in words:
            prefix = ""
            for char in word:
                prefix += char
                assert trie.prefix_search(prefix)
            assert trie.search(word)

    def test_delete(self):
        trie = Trie()
        trie.insert("hello")
        assert trie.search("hello")
        trie.delete("hello")
        assert not trie.search("hello")
        assert not trie.prefix_search("hell")

        trie.bulk_insert(("hello", "help"))
        trie.delete("hello")
        assert not trie.search("hello")
        assert not trie.prefix_search("hell")
        assert trie.search("help")
        assert trie.prefix_search("hel")

        trie.insert("a")
        assert trie.search("a")
        trie.delete("a")
        assert not trie.search("a")

    def test_delete_prefix(self):
        trie = Trie()
        words = ("a", "abc", "abd", "acd", "efg")
        trie.bulk_insert(words)
        for word in words:
            assert trie.search(word)

        trie.delete_prefix("ab")
        assert not trie.search("abc")
        assert not trie.search("abd")
        assert trie.search("a")
        assert trie.search("acd")
        assert trie.search("efg")
        trie.delete_prefix("a")
        for word in words:
            if word == "efg":
                assert trie.search(word)
            else:
                assert not trie.search(word)

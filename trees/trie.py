from data_structures.nodes.trie_node import TrieNode


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def bulk_insert(self, iterable):
        for word in iterable:
            self.insert(word)

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)

            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.is_end_of_word

    def prefix_search(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True

    def delete_prefix(self, prefix):
        current = self.root
        stack = []
        for char in prefix:
            if char in current.children:
                stack.append(current)
                current = current.children[char]
            else:
                return

        prev = stack.pop()
        del prev.children[current.char]
        current = prev
        while stack:
            prev = stack.pop()
            if not current.children:
                del prev.children[current.char]
                current = prev
            else:
                return

    def delete(self, word):
        current = self.root
        stack = []
        for char in word:
            if char in current.children:
                stack.append(current)
                current = current.children[char]
            else:
                return

        current.is_end_of_word = False
        while stack:
            prev = stack.pop()
            if not current.children:
                del prev.children[current.char]
                current = prev
            else:
                return

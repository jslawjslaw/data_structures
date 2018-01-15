
from .leaf_node import LeafNode
from .null_node import NullNode


class RootDeletionError(Exception):
    pass


class BinarySearchTree(object):

    def __init__(self, key, value=None):
        self.root = LeafNode(key, value)

    def insert(self, key, value=None):
        current_node = self.root
        previous_node = NullNode()
        direction = None
        while current_node:
            previous_node = current_node
            if current_node.key > key:
                current_node = current_node.left
                direction = "left"
            elif current_node.key == key:
                current_node.value = value
                return
            else:
                current_node = current_node.right
                direction = "right"

        new_node = LeafNode(key, value)
        setattr(previous_node, direction, new_node)

        return new_node

    def delete(self, key):
        if self.root.key == key:
            raise RootDeletionError("Cannot delete root node.")
        try:
            _, previous_node, direction = self._search(key)
            setattr(previous_node, direction, NullNode())
        except KeyError:
            pass

    def search(self, key):
        node, _, _ = self._search(key)
        return node

    def _search(self, key):
        node = self.root
        previous_node = None
        direction = None
        while node.key != key:
            previous_node = node
            if node.key > key:
                node = node.left
                direction = "left"
            else:
                node = node.right
                direction = "right"

            if not node:
                raise KeyError

        return node, previous_node, direction

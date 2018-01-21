
from data_structures.nodes.leaf_node import LeafNode
from data_structures.nodes.null_node import NullNode
from data_structures.trees.exceptions import RootDeletionError


class BinarySearchTree(object):

    def __init__(self, key, value=None):
        self.root = LeafNode(key, value)
        self.size = 1

    def __repr__(self):
        pass

    def insert(self, key, value=None):
        node = self.root
        predecessor = NullNode()
        direction = None
        while node:
            predecessor = node
            if node.key > key:
                node = node.left
                direction = "left"
            elif node.key == key:
                node.value = value
                return
            else:
                node = node.right
                direction = "right"

        new_node = LeafNode(key=key, value=value, predecessor=predecessor)
        setattr(predecessor, direction, new_node)
        self.size += 1

        return new_node

    def delete(self, key, drop_subtree=False):
        if self.root.key == key:
            raise RootDeletionError("Cannot delete root node.")

        try:
            node, direction = self._search(key)
            if drop_subtree:
                self._delete_drop_subtree(node, direction)
            else:
                self._delete(node, direction)
        except KeyError:
            pass

    def _delete(self, node, direction):
        if node.right and node.left:
            current_node = node.right
            while True:
                if current_node.left:
                    current_node = current_node.left
                else:
                    break
            if current_node.right:
                current_node.predecessor.left = current_node.right
            current_node.right = node.right
            current_node.left = node. left
            setattr(node.predecessor, direction, current_node)
        if node.left:
            setattr(node.predecessor, direction, node.left)
        if node.right:
            setattr(node.predecessor, direction, node.right)

        self._delete_drop_subtree(node, direction)

    def _delete_drop_subtree(self, node, direction):
        setattr(node.predecessor, direction, NullNode())

    def right_rotate(self, node):
        subtree_root = node.left.right
        current_node = node.right.left
        while True:
            if current_node.left:
                current_node = current_node.left
            else:
                break
        current_node.left = subtree_root
        node.predecessor.right = node.left
        if not node.predecessor:
            self.root = node.left
        node.left.right = node
        node.left = NullNode()

    def left_rotate(self, node):
        subtree_root = node.right.left
        current_node = node.left.right
        while True:
            if current_node.right:
                current_node = current_node.right
            else:
                break
        current_node.right = subtree_root
        node.predecessor.left = node.right
        if not node.predecessor:
            self.root = node.right
        node.right.left = node
        node.right = NullNode()

    def search(self, key):
        node, _ = self._search(key)
        return node

    def _search(self, key):
        node = self.root
        direction = None
        while node.key != key:
            if node.key > key:
                node = node.left
                direction = "left"
            else:
                node = node.right
                direction = "right"

            if not node:
                raise KeyError

        return node, direction

    def breadth_first_search(self, value):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return node

            if not isinstance(node.left, NullNode):
                queue.append(node.left)

            if not isinstance(node.right, NullNode):
                queue.append(node.right)

    def depth_first_search(self, value):
        if self.root.value == value:
            return self.root

        return self._depth_first_search(value, self.root)

    def _depth_first_search(self, value, node):
        if node.value == value:
            return node

        if isinstance(node, NullNode):
            return

        left = self._depth_first_search(value, node.left)
        right = self._depth_first_search(value, node.right)

        return left or right

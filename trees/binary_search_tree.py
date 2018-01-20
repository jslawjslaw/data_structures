
from data_structures.nodes.leaf_node import LeafNode
from data_structures.nodes.null_node import NullNode


class RootDeletionError(Exception):
    pass


class BinarySearchTree(object):

    def __init__(self, key, value=None):
        self.root = LeafNode(key, value)
        self.size = 1

    def __repr__(self):
        pass

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
        self.size += 1

        return new_node

    def delete(self, key, drop_subtree=False, left_rotate=True):
        if self.root.key == key:
            raise RootDeletionError("Cannot delete root node.")

        try:
            if drop_subtree:
                self._delete_drop_subtree(key)
            else:
                self._delete(key, left_rotate)
        except KeyError:
            pass

    def _delete(self, key, left_rotate):
        pass

    def _delete_drop_subtree(self, key):
        _, previous_node, direction = self._search(key)
        setattr(previous_node, direction, NullNode())

    def right_rotate(self, node, predecessor=NullNode()):
        pass

    def left_rotate(self, node, predecessor=NullNode()):
        right_left_subtree_root = node.right.left
        current_node = node.left.right
        while True:
            if current_node.right:
                current_node = current_node.right
            else:
                break
        current_node.right = right_left_subtree_root
        predecessor.left = node.right
        if not predecessor:
            self.root = node.right
        node.right.left = node
        node.right = NullNode()

    def search(self, key):
        node, _, _ = self._search(key)
        return node

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

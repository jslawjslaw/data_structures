
from nose.tools import assert_raises
from unittest import TestCase

from data_structures.trees.binary_search_tree import BinarySearchTree
from data_structures.trees.exceptions import RootDeletionError
from data_structures.nodes.null_node import NullNode


class TestBinarySearchTree(TestCase):

    def test_init(self):
        """Initializes with a root node; raises an error for empty key."""
        bst = BinarySearchTree(1, "value")

        assert bst.root.key == 1
        assert bst.root.value == "value"

        assert_raises(KeyError, BinarySearchTree, None, None)
        assert_raises(KeyError, BinarySearchTree, "string", None)

    def test_insert(self):
        """Inserts left children; inserts right children; replaces values;
        inserts at various levels.
        """
        bst = BinarySearchTree(1, "value")
        inserted_node_right = bst.insert(2, "higher value")
        inserted_node_left = bst.insert(0, "lower value")

        assert bst.root.right is inserted_node_right
        assert bst.root.left is inserted_node_left

        bst.insert(2, "some different value")
        assert bst.root.right.value == "some different value"

        rightmost_node = bst.insert(3, "an even higher value")
        assert bst.root.right.right is rightmost_node

    def test_delete(self):
        bst = BinarySearchTree(1)
        assert_raises(RootDeletionError, bst.delete, 1)

        inserted_node = bst.insert(2)
        assert bst.root.right is inserted_node

        bst.delete(2, drop_subtree=True)
        assert isinstance(bst.root.right, NullNode)

        bst.insert(8)
        new_predecessor = bst.insert(9)
        bst.insert(7)
        bst.insert(6)
        bst.insert(10)
        bst.delete(8)

        assert bst.root.right is new_predecessor
        assert bst.root.right.left.key == 7
        assert bst.root.right.left.predecessor is new_predecessor
        assert bst.root.right.right.key == 10
        assert_raises(KeyError, bst.search, 8)

        bst = BinarySearchTree(1)
        bst.insert(8)
        bst.insert(7)
        bst.insert(6)
        bst.insert(9)
        bst.insert(10)
        new_predecessor = bst.insert(8.5)
        bst.insert(8.75)
        bst.delete(8)

        assert bst.root.right is new_predecessor
        assert bst.root.right.right.key == 9
        assert bst.root.right.right.predecessor is new_predecessor
        assert bst.root.right.left.key == 7
        assert bst.root.right.right.left.key == 8.75
        assert_raises(KeyError, bst.search, 8)

    def test_search(self):
        bst = BinarySearchTree(1, "value")
        bst.insert(2, "another value")
        rightmost_node = bst.insert(3, "final value")

        node = bst.search(3)
        assert node is rightmost_node
        assert_raises(KeyError, bst.search, 5)

    def test_breadth_first_search(self):
        bst = BinarySearchTree(5, "apple")
        bst.insert(2, "banana")
        bst.insert(7, "orange")
        bst.insert(8, "tomato")
        node = bst.insert(6, "carrot")

        result = bst.breadth_first_search("carrot")
        assert node is result

        node = bst.breadth_first_search("hello")
        assert node is None

    def test_depth_first_search(self):
        bst = BinarySearchTree(5, "apple")
        bst.insert(2, "banana")
        bst.insert(7, "orange")
        bst.insert(8, "tomato")
        node = bst.insert(6, "carrot")

        result = bst.depth_first_search("carrot")
        assert node is result

        node = bst.depth_first_search("hello")
        assert node is None

    def test_left_rotate(self):
        bst = BinarySearchTree(5)
        node = bst.insert(6)
        bst.insert(4)
        bst.left_rotate(bst.root)

        assert bst.root is node
        assert bst.root.left.key == 5
        assert bst.root.left.left.key == 4

    def test_right_rotate(self):
        bst = BinarySearchTree(5)
        bst.insert(6)
        node = bst.insert(4)
        bst.right_rotate(bst.root)

        assert bst.root is node
        assert bst.root.right.key == 5
        assert bst.root.right.right.key == 6

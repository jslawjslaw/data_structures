
import numbers

from .null_node import NullNode


class LeafNode(object):

    def __repr__(self):
        rep = (
            "Key:         {} \n"
            "Value:       {} \n"
            "Left Child:  {} \n"
            "Right Child: {} \n"
            "Predecessor: {}"
        ).format(
            self.key,
            self.value,
            self.left.key,
            self.right.key,
            self.predecessor.key,
        )
        return rep

    def __init__(self, key, value=None, left=NullNode(), right=NullNode(),
                 predecessor=NullNode()):
        if key is None or not isinstance(key, numbers.Number):
            raise KeyError

        self.left = left
        self.right = right
        self._key = key
        self.value = value
        self.predecessor = predecessor

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if isinstance(key, numbers.Number):
            self._key = key
            return

        raise KeyError("Key: {} is not a number.".format(key))

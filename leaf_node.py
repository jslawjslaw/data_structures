
import numbers

from .null_node import NullNode


class LeafNode(object):

    def __repr__(self):
        rep = (
            "Key: {} \n"
            "Value: {} \n"
            "Left Child: {} \n"
            "Right Child: {} \n"
        ).format(self.key, self.value, self.left.key, self.right.key)
        return rep

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __init__(self, key, value=None, left=NullNode(), right=NullNode()):
        if key is None or not isinstance(key, numbers.Number):
            raise KeyError

        self.left = left
        self.right = right
        self._key = key
        self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if isinstance(key, numbers.Number):
            self._key = key
            return

        raise KeyError("Key: {} is not a number.".format(key))

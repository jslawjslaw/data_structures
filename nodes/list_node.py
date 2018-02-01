from .null_node import NullNode


class ListNode(object):

    def __init__(self, key, value, predecessor=NullNode(), child=NullNode()):
        self.key = key
        self.value = value
        self.predecessor = predecessor
        self.child = child

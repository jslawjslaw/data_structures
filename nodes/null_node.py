

class NullNode(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.key = None
        self.value = None
        self.predecessor = None

    @property
    def left(self):
        return None

    @left.setter
    def left(self, value):
        pass

    @property
    def right(self):
        return None

    @right.setter
    def right(self, value):
        pass

    @property
    def predecessor(self):
        return None

    @predecessor.setter
    def predecessor(self, value):
        pass

    def __nonzero__(self):
        return False

    # python 3 compatible
    def __bool__(self):
        return False

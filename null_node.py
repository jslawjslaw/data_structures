

class NullNode(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.key = None
        self.value = None

    def __nonzero__(self):
        return False

    # python 3 compatible
    def __bool__(self):
        return False

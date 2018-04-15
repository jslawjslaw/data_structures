

class TrieNode(object):

    def __init__(self, char=None):
        self.children = {}
        self.is_end_of_word = False
        self.char = char

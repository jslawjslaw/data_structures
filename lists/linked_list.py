from data_structures.nodes.list_node import ListNode


class LinkedList(object):

    def __init__(self):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None, predecessor=self.head)
        self.head.child = self.tail

    def insert(self, key, value):
        tail_predecessor = self.tail.predecessor
        new_node = ListNode(
            key,
            value,
            predecessor=tail_predecessor,
            child=self.tail,
        )
        tail_predecessor.child = new_node
        self.tail.predecessor = new_node

    def delete_by_key(self, key):
        node = self.search_by_key(key)
        if not node:
            return

        self._delete(node)

    def delete_by_value(self, value):
        node = self.search_by_value(value)
        if not node:
            return

        self._delete(node)

    def _delete(self, node):
        predecessor = node.predecessor
        child = node.child
        predecessor.child = child
        child.predecessor = predecessor

    def search_by_key(self, key):
        current_node = self.head
        while current_node.key != key:
            current_node = current_node.child

            if current_node is self.tail:
                return

        return current_node

    def search_by_value(self, value):
        current_node = self.head
        while current_node.value != value:
            current_node = current_node.child

            if current_node is self.tail:
                return

        return current_node

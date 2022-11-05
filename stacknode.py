class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top == None

    def __len__(self):
        return self._size

    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack."
        return self._top.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1

    def pop(self):
        assert not self.isEmpty(), "Cannot pop an empty stack"
        node = self._top

        self._top = self._top.next
        self._size = -1
        return node.item

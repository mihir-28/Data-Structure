class _BagListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class Bag:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, target):
        curNode = self._head
        while curNode != None and curNode.item != target:
            curNode = curNode.next
        return curNode != None

    def add(self, item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def remove(self, item):
        predNode = None
        curNode = self._head

        while curNode != None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next

        assert curNode is not None, "The item must be in the bag."

        self._size -= 1
        if curNode == self._head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next
        return curNode.item

    def printBagElements(self):
        for e in self:
            print(e)

    def __iter__(self):
        return _BagIterator(self._head)

class _BagIterator:
    def __init__(self, listHead):
        self._curNode = listHead

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNode == None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item

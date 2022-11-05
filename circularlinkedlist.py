class CListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CList:
    def __init__(self):
        self._listRef = None

    def traversal(self):
        if self._listRef != None:
            curNode = self._listRef
            while True:
                curNode = curNode.next
                print(curNode.data)
                if curNode == self._listRef:
                    break
        return

    def search(self, value):
        if self._listRef != None:
            curNode = self._listRef
            while True:
                curNode = curNode.next
                if curNode.data == value:
                    return True
                if curNode == self._listRef:
                    return False
        return False

    def addNode(self, value):
        newNode = CListNode(value)
        if self._listRef == None:
            self._listRef = newNode
            newNode.next = newNode
        elif value < self._listRef.next.data:
            newNode.next = self._listRef.next
            self._listRef.next = newNode
        elif value > self._listRef.data:
            newNode.next = self._listRef.next
            self._listRef.next = newNode
            self._listRef = newNode
        else:
            predNode = None
            curNode = self._listRef.next
            while curNode != self._listRef and curNode.data < value:
                predNode = curNode
                curNode = curNode.next
                
            newNode.next = curNode
            predNode.next = newNode

    def removeNode (self, value):
        assert self._listRef != None, "Cannot remove from empty list"
        if self._listRef == value and self._listRef == self._listRef.next:
            self._listRef = None
        else:
            predNode = self._listRef
            curNode = self._listRef.next
            while curNode != self._listRef and curNode.data != value:
                predNode = curNode
                curNode = curNode.next
            assert curNode.data == value, "Element not in the list"
            predNode.next = curNode.next

            if curNode == self._listRef:
                self._listRef = predNode
        return value
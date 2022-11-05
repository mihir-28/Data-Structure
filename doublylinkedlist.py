class DListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._probe = None

    def traversal(self):
        curNode = self._head
        while curNode != None:
            print(curNode.data)
            curNode = curNode.next

    def revTraversal(self):
        curNode = self._tail
        while curNode != None:
            print(curNode.data)
            curNode = curNode.prev

    def search(self, value):
        if self._head == None:
            return False

        elif self._probe == None:
            self._probe = self._head

        if value < self._probe.data:
            while self._probe != None and value <= self._probe.data:
                if value == self._probe.data:
                    return True
                else:
                    self._probe = self._probe.prev
        else:
            while self._probe != None and value >= self._probe.data:
                if value == self._probe.data:
                    return True
                else:
                    self._probe = self._probe.next
            return False

    def addNode(self, value):
        newNode = DListNode(value)
        if self._head == None:
            self._head = newNode
            self._tail = self._head

        elif value < self._head.data:
            newNode.next = self._head
            self._head.prev = newNode
            self._head = newNode

        elif value > self._tail.data:
            newNode.prev = self._tail
            self._tail.next = newNode
            self._tail = newNode

        else:
            curNode = self._head
            while curNode != None and curNode.data < value:
                curNode = curNode.next

            newNode.next = curNode
            newNode.prev = curNode.prev
            curNode.prev.next = newNode
            curNode.prev = newNode

    def removeNode(self, value):
        assert self.search(value), "Element not in the list"
        if self._probe == self._head:
            if self._head == self._tail:
                self._head = None
                self._tail = None

            else:
                self._head = self._head.next
                self._head.prev = None

        elif self._tail == self._probe:
            self._tail = self._tail.prev
            self._tail.next = None

        else:
            self._probe.prev.next = self._probe.next
            self._probe.next.prev = self._probe.prev
        
        self._probe = None
        return value

class _QNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._head == None

    def enqueue(self, x):
        newNode = _QNode(x)
        if self._head == None:
            self._head = newNode
        else:
            self._tail.next = newNode
        
        self._tail = newNode
        self._size += 1

    def first(self):
        assert not self.isEmpty(), "Cannot remove from an empty queue"
        return self._head.data
    
    def dequeue(self):
        assert not self.isEmpty(), "Cannot remove from an empty queue"
        x = self._head.data
        self._head = self._head.next
        if self.isEmpty():
            self._tail = None
        
        self._size -= 1
        return x

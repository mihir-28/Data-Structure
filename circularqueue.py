from arrayadt import Array

class CQueue:
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = Array(maxSize)

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == len(self._qArray)

    def __len__(self):
        return self._count

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue"
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item


"""
>>> q = Queue(7)
>>> q.enqueue(31)
>>> q.enqueue(54)
>>> q.enqueue(83)
>>> q.enqueue(67)
>>> q.enqueue(51)
>>> q.enqueue(20)
>>> q.enqueue(75)
>>> q.isFull()
True
>>> q.isEmpty()
False
>>> q.dequeue()
31
>>> q.dequeue()
54
>>> len(q)
5
>>> q.dequeue()
83
>>> q.dequeue()
67
>>> q.dequeue()
51
>>> q.dequeue()
20
>>> q.dequeue()
75
>>> len(q)
0
>>> q.isFull()
False
>>> q.isEmpty()
True
"""
from arrayadt import Array
from queuenode import Queue


class BPriorityQueue:
    def __init__(self, numLevels):
        self._qsize = 0
        self._qlevels = Array(numLevels)
        for i in range(numLevels):
            self._qlevels[i] = Queue()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._qsize

    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self._qlevels), \
            "Invalid priority level"
        self._qlevels[priority].enqueue(item)
        self._qsize += 1

    def dequeue(self):
        assert not self.isEmpty(), \
            "Cannot dequeue from an empty queue"
        i = 0
        p = len(self._qlevels)
        while i < p and self._qlevels[i].isEmpty():
            i += 1
        self._qsize -= 1
        return self._qlevels[i].dequeue()


"""
>>> q=BPriorityQueue(5)
>>> q.enqueue("White", 3)
>>> q.enqueue("Blue",2)
>>> q.enqueue("Black",5)
AssertionError: Invalid priority level
>>> q.enqueue("Black",4)
>>> q.enqueue("Green",1)
>>> q.enqueue("Cyan",0)
>>> q.enqueue("Orange",2)
>>> q.enqueue("Orange",4)
>>> q.enqueue("Coral",4)
>>> q.isEmpty()
False
>>> len(q)
8
>>> q.dequeue()
'Cyan'
>>> q.dequeue()
'Green'
>>> q.dequeue()
'Blue'
>>> len(q)
5
"""
class _priorityQEntry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


class priorityQueue:
    def __init__(self):
        self._qlist = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._qlist)

    def enqueue(self, item, priority):
        entry = _priorityQEntry(item, priority)
        self._qlist.append(entry)

    def dequeue(self):
        assert not self.isEmpty(), \
            "Cannot dequeue from an empty queue"
        highest = 0
        for i in range(len(self)):
            if self._qlist[i].priority < self._qlist[highest].priority:
                highest = i
            entry = self._qlist.pop(highest)
            return entry.item




"""
>>> p = priorityQueue()
>>> p.enqueue("Blue",2)
>>> p.enqueue("Yellow",6)
>>> p.enqueue("Black",5)
>>> p.enqueue("Red",4)
>>> p.enqueue("White",1)
>>> p.enqueue("Green",3)
>>> len(p)
6
>>> p.isEmpty()
False
>>> p.dequeue()
'White'
>>> p.dequeue()
'Blue'
>>> p.dequeue()
'Green'
>>> p.dequeue()
'Red'
>>> p.dequeue()
'Black'
>>> p.dequeue()
'Yellow'
>>> p.dequeue()
AssertionError: Cannnot dequeue from an empty queue
>>> len(p)
0
"""
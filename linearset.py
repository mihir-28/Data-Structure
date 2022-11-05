class Set:
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def __contains__(self, e):
        return e in self._theElements   

    def add(self, e):                  
        if e not in self :
            self._theElements.append(e)   

    def remove(self, e):
        assert e in self, "The element must be in the set."
        self._theElements.remove(e)

    def __eq__(self, setB):                 
        if len(self) != len(setB) :
            return False
        else :
            return self.isSubsetOf(setB)

    def isSubsetOf(self,setB):
        for e in self:
            if e not in setB:
                return False
        return True

    def union(self,setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for e in setB:
            if e not in self:
                newSet._theElements.append(e)
        return newSet

    def difference(self, setB):
        newSet = Set()
        # newSet._theElements.extend(self._theElements)
        # for element in setB:
        #     if element in self:
        #         newSet._theElements.remove( element )
        for element in self:
            if element not in setB:
                newSet._theElements.append(element)
        return newSet

    def intersection(self, setB):
        newSet = Set()
        for element in setB:
            if element in self:
                newSet._theElements.append(element)
        return newSet

    def __iter__(self):
        return _SetIterator(self._theElements)

class _SetIterator:
    def __init__(self, elements):
        self._setElements = elements
        self._curItem = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curItem < len(self._setElements):
            e = self._setElements[self._curItem]
            self._curItem += 1
            return e
        else: 
            raise StopIteration
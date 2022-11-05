class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self._root = None
        self._size = 0
    
    def search_node(self, x):
        found = False
        t = self._root
        while t != None and not found:
            if x == t.data:
                found = True
            elif x < t.data:
                t = t.left
            else:
                t = t.right
        if not found:
            return None
        else:
            return t

    def insert_node(self, x):
        found = False
        p = self._root
        q = None
        while p != None and not found:
            q = p
            if x == p.data:
                found = True
            elif x < p.data:
                p = p.left
            else:
                p = p.right
        if not found:
            p = Node(x)
            p.parent = q
            if self._root != None:
                if x < q.data:
                    q.left = p
                else:
                    q.right = p
            else:
                self._root = p
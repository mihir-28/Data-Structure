class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None

    def traversal(self):
        curNode = self._head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    def unorderedSearch(self, target):
        curNode = self._head
        while curNode != None and curNode.data != target:
            curNode = curNode.next
        return curNode != None

    def prependNode(self, item):
        newNode = ListNode(item)
        newNode.next = self._head
        self._head = newNode

    def removeNode(self, target):
        predNode = None
        curNode = self._head
        while curNode != None and curNode.data != target:
            predNode = curNode
            curNode = curNode.next

        if curNode != None:
            if curNode == self._head:
                self._head = curNode.next
            else:
                predNode.next = curNode.next

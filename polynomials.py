class _PolyTermNode:
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None


class Polynomial:
    def __init__(self):
        self._polyHead = None
        self._polyTail = None

    def degree(self):
        if self._polyHead == None:
            return -1
        else:
            return self._polyHead.degree

    def appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead == None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm

            self._polyTail = newTerm

    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non-empty polynomials can be evaluated."

        result = 0.0

        curNode = self._polyHead
        while curNode != None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next

        return result

    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."

        curNode = self._polyHead
        while curNode != None and curNode.degree != degree:
            curNode = curNode.next

        if curNode == None:
            return 0.0
        else:
            return curNode.coefficient

    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
            "Addition only allowed on non-empty polynomials."

        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        while nodeA != None and nodeB != None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree  # or degree = nodeB.degree
                value = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly.appendTerm(degree, value)

        while nodeA != None:
            newPoly.appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB != None:
            newPoly.appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def __sub__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
            "Substraction only allowed on non-empty polynomials."

        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = -nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree  # or degree = nodeB.degree
                value = nodeA.coefficient - nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly.appendTerm(degree, value)

        while nodeA != None:
            newPoly.appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB != None:
            newPoly.appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def __mul__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0,\
            "Multiplication only allowed on non-empty polynomials."

        node = self._polyHead
        newPoly = rhsPoly._termMultiply(node)

        node = node.next
        while node != None:
            tempPoly = rhsPoly._termMultiply(node)
            newPoly += tempPoly
            node = node.next

        return newPoly

    def _termMultiply(self, termNode):
        newPoly = Polynomial()

        curr = self._polyHead
        while curr != None:
            newDegree = curr.degree + termNode.degree
            newCoefficient = curr.coefficient * termNode.coefficient
            newPoly.appendTerm(newDegree, newCoefficient)
            curr = curr.next

        return newPoly

    def printPoly(self):
        curNode = self._polyHead
        while curNode is not None:
            print(curNode.degree, curNode.coefficient)
            curNode = curNode.next
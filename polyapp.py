from polynomials import *

P1 = Polynomial()
P1.appendTerm(2,5)
P1.appendTerm(1,3)
P1.appendTerm(0,-10)

print("P1:")
P1.printPoly()
print()

print("Evaluation Of Poynomial P1 At 2: ", P1.evaluate(2))
print()

P2 = Polynomial()
P2.appendTerm(3,2)
P2.appendTerm(2,4)
P2.appendTerm(0,3)

print("P2:")
P2.printPoly()
print()

print("Degree Of Poynomial P2: ", P2.degree())
print()

P3 = P1 + P2
print("P3 = P1 + P2:")
P3.printPoly()
print()

P4 = P1 - P2
print("P4 = P1 - P2:")
P4.printPoly()
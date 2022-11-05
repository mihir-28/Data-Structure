from linearset import *

A = Set()
A.add(1)
A.add(5)
A.add(7)
A.add(9)
print("Length of Set A: ", len(A))

B = Set()
B.add(2)
B.add(3)
B.add(7)
B.add(9)
print("Length of Set B: ", len(B))

print("\nElements of Set A: ")
for e in A:
    print(e)

print("\nElements of Set B: ")
for e in B:
    print(e)

print("\nIs 4 in B: ", 4 in B)

print("Is Set A equal to Set B: ", A == B)

B.remove(2)
print("\nSet B after removing element 2: ")
for e in B:
    print(e)

print("\nIs B subset of A: ", B.isSubsetOf(A))

print("Is A subset of B: ", A.isSubsetOf(B))

D = A.intersection(B)
print("\nIntersection of Set A & Set B: ")
for e in D:
    print(e)

E = A.difference(B)
print("\nDifference of Set A & Set B: ")
for e in E:
    print(e)

F = B.difference(A)
print("\nDifference of Set B & Set A: ")
for e in F:
    print(e)
from bagadt import *

myBag = Bag()
myBag.add(78)
myBag.add('Hello')
myBag.add(54)
myBag.add(96.4)
myBag.add("String")

print(len(myBag))
print('\n')

for i in myBag:
    print(i)

print('\n')

myBag.remove(54)

for i in myBag:
    print(i)
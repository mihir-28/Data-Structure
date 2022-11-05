from linkedlistbag import *

myBag = Bag()
myBag.add(78)
myBag.add(84)
myBag.add(54)
myBag.add(96)
myBag.add(65)

print('No of elements in Bag: ', len(myBag))
myBag.printBagElements()
print()

value = int(input('Guess A value in Bag: '))
if value in myBag:
    print("The Bag Contains the value")
else:
    print("The Bag does not Contains the value")
print()

myBag.remove(84)
print("Bag Elements After Removing 84: ")
myBag.printBagElements()
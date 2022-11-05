from bagadt import *

myBag = Bag()
myBag.add(78)
myBag.add(84)
myBag.add(54)
myBag.add(96)
myBag.add(65)

print('No of Items in Bag: ', len(myBag))
myBag.printBagElements()

value = int(input('Guess A value Contained in the Bag: '))
if value in myBag:
    print("The Bag Contains the value")
else:
    print("The Bag does not Contains the value")

myBag.remove(84)
myBag.printBagElements()
from singlylinkedlist import *

ll = LinkedList()
print('1: Add an element')
print('2: Traverse the list')
print('3: Search an element')
print('4: Remove an element')
print('5: Exit')
print()

while True:
    ch = int(input('Enter a choice(1-5): '))
    if ch == 1:
        ele = input('Enter an element to be added: ')
        ll.prependNode(ele)
        print()

    elif ch == 2:
        ll.traversal()
        print()

    elif ch == 3:
        ele = input('Enter element to search: ')
        if ll.unorderedSearch(ele):
            print('Element Found')
        else:
            print('Element Not Found')
        print()

    elif ch == 4:
        ele = input('Enter an element to remove: ')
        ll.removeNode(ele)
        print()

    elif ch == 5:
        break

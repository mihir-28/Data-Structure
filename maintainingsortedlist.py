def findSortedPosition(theList, target):
    low = 0
    high = len(theList) - 1
    while low <= high:
        mid = (high + low) // 2
        if theList[mid] == target:
            return mid
        elif target < theList[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

l = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
l.sort()
print('List: ', l)
x = int(input('\nEnter A Number To Find Input Position: '))
res = findSortedPosition(l, x)
print('The Number Will Be Inserted At Index Position: ', res)
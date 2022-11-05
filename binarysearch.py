def binarySearch(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low) // 2
        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


l = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
l.sort()
x = int(input('Enter A Number To Search: '))
res = binarySearch(l, x)
if res == True:
    print('Number Found')
else:
    print('Number not Found')
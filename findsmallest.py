def findSmallest(theValues):
    n = len(theValues)
    smallest = theValues[0]
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest


l = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print('List: ', l)
res = findSmallest(l)
print('Smallest in the list: ', res)
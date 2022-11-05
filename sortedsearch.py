def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == item:
            return True
        elif theValues[i] > item:
            return False
    return False


l = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
l.sort()
x = int(input('Enter A Number To Search: '))
res = sortedLinearSearch(l, x)
if res == True:
    print('Number Found')
else:
    print('Number not Found')
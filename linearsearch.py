def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
    return False


l = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
x = int(input('Enter A Number To Search: '))
res = linearSearch(l, x)
if res == True:
    print('Number Found')
else:
    print('Number not Found')
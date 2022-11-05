def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        smallNdx = i
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
    
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp

inp = input("Enter Elements Separated By Comma: \n")
inpList = inp.split(',')
l = []
for x in inpList:
    l.append(int(x))

selectionSort(l)
print("\nSorted List: \n", l)

"""l = []
x = int(input("Enter The Number Of Elements: "))
print("Enter The Elements: ")
for i in range(x):
    a = int(input())
    l.append(a)

selectionSort(l)
print("\nSorted List: ", l)"""
# print("\nSorted List: ")
# for i in l:
#     print(i)
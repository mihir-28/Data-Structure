def bubbleSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

l = []
x = int(input("Enter The Number Of Elements: "))
print("Enter The Elements: ")
for i in range(x):
    a = int(input())
    l.append(a)

bubbleSort(l)
print("\nSorted List: ")
for i in l:
    print(i)
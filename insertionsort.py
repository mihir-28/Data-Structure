def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value

l = []
x = int(input("Enter The Number Of Elements: "))
print("Enter The Elements: ")
for i in range(x):
    a = int(input())
    l.append(a)

insertionSort(l)
print("\nSorted List: ", l)
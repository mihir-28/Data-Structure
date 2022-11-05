def recBinarySearch(target, values, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if values[mid] == target:
            return True
        elif target < values[mid]:
            return recBinarySearch(target, values, low, mid - 1)
        else:
            return recBinarySearch(target, values, mid + 1, high)


l = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 65]
x = int(input("Enter Number To Search: "))
r = recBinarySearch(x, l, 0, len(l) - 1)
print("Element Present?", r)
def heapsort(a):
    n = len(a) - 1
    for i in range((n-1)//2, -1, -1):
        adjust(a, i, n)
    
    for k in range(n, 0, -1):
        t = a[k]
        a[k] = a[0]
        a[0] = t
        adjust(a, 0, k - 1)
def move(n, src, dest, temp):
    if n >= 1:
        move(n - 1, src, temp, dest)
        print("Move %d -> %d" % (src, dest))
        move(n - 1, temp, dest, src)

d = int(input("Enter Number Of Disks: "))
move(d, 1, 3, 2)
# my = Array(3)
# >>> my[0] = 1
# >>> my[1] = 2
# >>> my[2] = 3
# >>> len(my)
# >>> my.clear(0)
# >>> for i in my:
# 	print(i)

from arrayadt import Array

theCounters = Array(123)
thefile = open('data.txt', 'r+')
for line in thefile:
    for letter in line:
        code = ord(letter)
        theCounters[code] += 1
thefile.close()

for i in range(26):
    print(chr(65+i), theCounters[65+i], \
        chr(97+i), theCounters[97+i])
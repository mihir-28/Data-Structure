from linearmap import *

m = Map()
m.add('John', 78)
m.add('Brec', 85)
m.add('Jacob', 96)
m.add('Elle', 100)

print("Map M: ")
for e in m:
    print(e.key, ":", e.value)

print("\nLength of Map M: ", len(m))
print("Is Brec in Map M: ", 'Brec' in m)
print("Value of Elle: ", m.valueOf('Elle'))

m.remove('John')
print("\nMap M after removing key John: ")
for e in m:
    print(e.key, ":", e.value)

print(m._findPosition('Brec'))

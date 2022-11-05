from stack import *

s = Stack()

s.push(21)
s.push(-1)
s.push(67)
s.push(10)
s.push(67)

print("Length of the stack:",len(s))
print(s.isEmpty())
print("Top of the stack element:",s.peek())

print("\nPopping out all the elements")
s.pop()
print(len(s))
s.pop()
print(len(s))
s.pop()
print(len(s))
s.pop()
print(len(s))
s.pop()
print(len(s))
print(s.isEmpty())
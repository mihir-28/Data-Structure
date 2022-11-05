def fib(n):
    assert n >= 0, "Fibonacci not defined for n < 0"
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

x=int(input("Enter Number For nth Term Of Fibonacci: "))
print("%dth Term Of Fibocacci is: %d" %(x, fib(x)))

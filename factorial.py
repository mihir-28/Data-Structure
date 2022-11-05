def fact(n):
    assert n >= 0, "Factorial is not defined for negative values."
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

x=int(input("Enter Number For Factorial: "))
print("Factorial of %d is: %d" %(x, fact(x)))
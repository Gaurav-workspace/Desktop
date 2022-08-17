def Factorial(n,m):
    if m==n:
        return 1
    else:
        return n*Factorial(n-1,m)

print(Factorial(5,2))
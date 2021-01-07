def fact1(n):
    if n==0:
        return 1
    return n*fact1(n-1)
res=fact1(int(input('enter a number : ')))
print(res)

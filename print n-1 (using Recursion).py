def rev(n):
    if n<=0:
        return
    else:
        print(n, end=" ")
        rev(n-1)
n=int(input())
rev(n)

def printNumber(n):
  if n > 0:
    printNumber(n-1)
    print(n, end = ' ')
    
n =int(input())
printNumber(n)

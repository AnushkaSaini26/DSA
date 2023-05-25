def findMax(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMax(A, n - 1))
arr=[]
n = int(input("Enter the size of the array: "))
print("Enter the Elements of the array:")
for i in range(0,n):
    num = int(input())
    arr.append(num)
print(findMax(arr, n))    

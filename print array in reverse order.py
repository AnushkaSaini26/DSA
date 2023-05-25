def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
arr=[]
n = int(input("Enter the size of the array: "))
print("Enter the Elements of the array:")
for i in range(0,n):
    num = int(input())
    arr.append(num)
reverseList(arr,0,n-1)    
print("Reversed array:")
print(arr)

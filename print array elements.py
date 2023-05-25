def PrintArray(arr,i,n):
    if(i>=n):
        return
    print(arr[i],end=" ")
    PrintArray(arr,i+1,n)
arr=[]
n = int(input("Enter the size of the array: "))
print("Enter the Elements of the array:")
for i in range(0,n):
    num = int(input())
    arr.append(num)

print("Array Element:")
PrintArray(arr,0,n)

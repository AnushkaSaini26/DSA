def nser(arr, n):

    stack = []
    ans = []
    arr = arr[::-1]
    for i in arr:
        while stack:
            if stack[-1] < i:
                ans.append(stack[-1])
                break
            else:
                stack.pop()
        if not stack:
            ans.append(-1)
        stack.append(i)
            
    return ans[::-1]

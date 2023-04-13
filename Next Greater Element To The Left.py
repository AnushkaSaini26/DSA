def ngel(arr,n):
  ans= []
  for i in range(0, n):
    for j in range(i-1, -1, -1):
      if arr[i] < arr[j]:
        ans.append(arr[j])
        break
    else:
      ans.append(-1)
  return ans

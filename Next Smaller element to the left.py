def nsel(n, arr):
    lst=[-1]
    res=[]
    for i in range(n):
            
        while lst and lst[-1]>=arr[i]:
            lst.pop()
                
        res.append(lst[-1])
        lst.append(arr[i])
            
    return res

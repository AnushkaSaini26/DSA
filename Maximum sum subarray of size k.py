class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        start=0
        end=0
        s=0
        ans=0
        while (end<N):
            s+=Arr[end]
            if ((end-start+1) == K):
                ans=max(ans,s)
                s-=Arr[start]
                start+=1
            end+=1    
        return ans

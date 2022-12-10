class Solution:
    
    def checkIsAP(self, arr, n):
        if (n == 1):
            return True
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2,n):
            if (arr[i] - arr[i-1] != diff):
                return False
        return True

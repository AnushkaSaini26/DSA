class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
          
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        m = 1
        while(xor&m == 0):
            m= m << 1
        for num in nums:
            if num&m:
                a ^= num
            else:
                b ^= num
        return [a, b]

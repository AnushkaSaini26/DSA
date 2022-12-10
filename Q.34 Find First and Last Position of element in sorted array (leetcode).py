class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def FirstOccurrence(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = left + (right - left) // 2
                if target == nums[mid]:
                    first = mid
                    right = mid - 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return first


        def LastOccurrence(nums, target):
            left, right = 0, len(nums) - 1
            last= -1
            while left <= right:
                mid = left + (right - left) // 2
                if target == nums[mid]:
                    last= mid
                    left =mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return last

        return [FirstOccurrence(nums,target),LastOccurrence(nums,target)]

    
    
            

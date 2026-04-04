class Solution:
    def findMin(self, nums: List[int]) -> int:
        #### O(n)
        
        return min(nums)
        
        #### O(log n)

        # left = 0
        # right = len(nums)-1 
        # while left < right:
        #     mid = (left+right)//2
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid
            
        # return nums[right]
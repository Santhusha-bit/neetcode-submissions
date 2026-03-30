class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(set(nums))
        max = 0
        left=0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                right = i+1
                diff=right-left
                if max < diff:
                    max = diff 
            else:
                left=i+1
        return max+1
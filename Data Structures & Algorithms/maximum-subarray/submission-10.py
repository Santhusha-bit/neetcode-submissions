class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return nums[0]
        lsts =[]
        for l in range(len(nums)):
            for r in range(1,len(nums)+1):
                if nums[l:r] != []:
                    lsts.append(sum(nums[l:r]))
            
        return max(lsts)
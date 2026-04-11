class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            currSum += nums[i]
            result = max(result, currSum, nums[i])
            if currSum < 0:
                currSum = 0
        
        return result

        # val = float("-inf") 
        # if len(nums) <=1:
        #     return nums[0]
        # lsts =[]
        # for l in range(len(nums)):
        #     for r in range(1,len(nums)+1):
        #         if nums[l:r] != []:
        #             val = max(val, sum(nums[l:r]))
            
        # return val
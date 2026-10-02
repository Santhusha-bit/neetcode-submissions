class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l = 0
        nums = list(set(nums))
        nums.sort()

        maxAdd = 1
        add = 1
        for r in range(1, len(nums)):
            if nums[l]+1 == nums[r]:
                add += 1
                l += 1
            else:
                add = 1
                l+=1
            maxAdd = max(add, maxAdd)

        return maxAdd
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums) == 0:
        #     return 0
        # nums = sorted(set(nums))
        # maxi = 1
        # current = 1
        # for i in range(len(nums)-1):
        #     if nums[i]+1 == nums[i+1]:
        #         current+=1
        #         if maxi < current:
        #             maxi=current
        #     else:
        #         current=1
        # return maxi

        
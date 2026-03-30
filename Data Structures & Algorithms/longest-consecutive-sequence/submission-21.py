class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # nums = sorted(set(nums))
        # maxi = 0
        # left=0
        # for i in range(len(nums)-1):
        #     if nums[i]+1 == nums[i+1]:
        #         right = i+1
        #         diff=right-left
        #         if maxi < diff:
        #             maxi=diff 
        #     else:
        #         left=i+1
        # return maxi+1
        nums = sorted(set(nums))
        maxi = 1
        current = 1
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                current+=1
                if maxi < current:
                    maxi=current
            else:
                current=1
        return maxi
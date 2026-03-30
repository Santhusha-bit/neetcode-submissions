class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                longest = max(longest, length)

        return longest
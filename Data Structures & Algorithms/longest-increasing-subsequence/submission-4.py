class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # how many numbers >= than me
        if len(nums) == 1:
            return 1

        dp = [1]*len(nums)


        for i in range(len(nums)-1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
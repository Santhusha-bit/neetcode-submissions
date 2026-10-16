class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False

        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
            print(nextDP)

        return True if target in dp else False




class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # best = max(nums)

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(i, len(nums)):
        #         prod *= nums[j]
        #         best = max(best, prod)

        # return best

        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n 
            curMax = max(tmp, n*curMin)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        return res
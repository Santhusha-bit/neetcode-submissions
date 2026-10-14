import math

class Solution:
    def maxProduct(self, nums: List[int]):        
        res = max(nums)
        curMax = 1
        curMin = 1

        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            tmp = curMax * n 
            curMax = max(tmp, n*curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        return res
        
    

        
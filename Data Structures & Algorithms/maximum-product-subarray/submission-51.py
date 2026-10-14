import math

class Solution:
    def maxProduct(self, nums: List[int]): 
        res = max(nums)
        curMin = 1
        curMax = 1

        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
                continue
            tmp = curMax * n
            curMax = max(tmp, curMin*n)
            curMin = min(tmp, curMin*n, n)
            res= max(res, curMax)

        return res        
    

        
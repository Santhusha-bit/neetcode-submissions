import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            dummy=nums.copy()
            dummy.remove(nums[i])
            res.append(math.prod(dummy))

        return res
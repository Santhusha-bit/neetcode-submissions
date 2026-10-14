class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) > 2:
            def inner(subArray):
                rob1, rob2 = 0, 0

                for n in subArray:
                    temp = max(rob1+n, rob2)
                    rob1 = rob2
                    rob2 = temp

                return rob2

            return max(inner(nums[:-1]), inner(nums[1:]))
        
        else:
            return max(nums)
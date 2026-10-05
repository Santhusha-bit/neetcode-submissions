class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(subset[:])
                return

            if i>= len(nums) or remaining < 0:
                return

            subset.append(nums[i])
            backtrack(i, remaining - nums[i])

            subset.pop()

            backtrack(i+1, remaining)

        backtrack(0, target)
        return res
                    
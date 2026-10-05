class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(subset[:])
                return

            if i >= len(candidates) or remaining < 0 or candidates[i] > target:
                return 

            subset.append(candidates[i])
            backtrack(i+1, remaining-candidates[i])

            while i+1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            subset.pop()
            backtrack(i+1, remaining)

        backtrack(0, target)
        return res
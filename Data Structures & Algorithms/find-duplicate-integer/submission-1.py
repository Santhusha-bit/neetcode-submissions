class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = Counter(nums)

        out = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return out[0][0]


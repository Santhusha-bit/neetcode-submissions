class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()
        for n in range(0, len(nums)):
            if nums[n] in unique:
                return nums[n]
            else:
                unique.add(nums[n])

        # d = Counter(nums)
        # out = sorted(d.items(), key=lambda item: item[1], reverse=True)
        # return out[0][0]


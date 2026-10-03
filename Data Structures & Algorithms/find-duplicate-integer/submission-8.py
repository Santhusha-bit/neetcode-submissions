class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # METHOD 3
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow 



        # METHOD 2
        # unique = set()
        # for n in range(0, len(nums)):
        #     if nums[n] in unique:
        #         return nums[n]
        #     else:
        #         unique.add(nums[n])

        # METHOD 1
        # d = Counter(nums)
        # out = sorted(d.items(), key=lambda item: item[1], reverse=True)
        # return out[0][0]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        d = set()
        for n in nums:
            if n not in d:
                d.add(n)
            else:
                d.remove(n)

        return d.pop()
                        

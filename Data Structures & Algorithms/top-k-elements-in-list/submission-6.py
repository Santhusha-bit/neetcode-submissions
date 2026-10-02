class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        s = dict.most_common(k)
        res = [r[0] for r in s]
        return res

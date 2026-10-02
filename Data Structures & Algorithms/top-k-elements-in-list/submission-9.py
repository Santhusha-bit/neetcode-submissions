class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        s = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        res = [r[0] for r in s][:k]
        return res


        # s = dict.most_common(k)
        # res = [r[0] for r in s]
        # return res

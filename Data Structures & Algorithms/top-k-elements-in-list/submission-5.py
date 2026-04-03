class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        out = []
        for i in nums:    
            dic[i] = dic.get(i, 0) + 1
            
        out = sorted(dic, key=dic.get, reverse=True)
        return out[:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        out = []
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        out = sorted(dic, key=dic.get, reverse=True)
        return out[:k]

            

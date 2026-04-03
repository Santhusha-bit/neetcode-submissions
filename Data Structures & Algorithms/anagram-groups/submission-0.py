class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            if "".join(sorted(s)) not in dic:
                dic["".join(sorted(s))] = [s]
            else:
                dic["".join(sorted(s))].append(s)
        return list(dic.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            dict[key].append(w)

        return [v for v in dict.values()]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def bt(start):
            if start >= len(s):
                if "".join(subset[:]) == s:
                    res.append(subset[:])
                return 

            for end in range(start, len(s)):
                word = s[start:end +1]

                if word == word[::-1]:
                    subset.append(word)
                    bt(end+1)
                    subset.pop()

        bt(0)
        return res
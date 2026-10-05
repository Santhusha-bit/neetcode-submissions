class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z'],
        }

        res = []
        subset = []

        def bt(i):
            if len(subset[:]) == len(digits):
                res.append("".join(subset[:]))
                return

            for letter in d[int(digits[i])]:
                subset.append(letter)
                bt(i+1)
                subset.pop()

        if digits:
            bt(0)
        return res
        
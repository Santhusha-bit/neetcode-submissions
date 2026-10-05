class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        }

        res = []
        subset = []

        def bt(i):
            if len(subset[:]) == len(digits):
                res.append("".join(subset[:]))
                return

            for letter in d[digits[i]]:
                subset.append(letter)
                bt(i+1)
                subset.pop()

        if digits:
            bt(0)
        return res
        
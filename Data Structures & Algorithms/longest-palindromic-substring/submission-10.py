class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        out = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if len(out) < len(s[i:j+1]):
                        out = s[i:j+1]
        return out
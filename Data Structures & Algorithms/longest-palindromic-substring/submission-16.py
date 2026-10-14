class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        out = ""

        for i in range(len(s)):
            l = r = i
            while 0 <= l and r <len(s) and s[l] == s[r]:
                if r-l+1 > len(out):
                    out = s[l:r+1]
                l-=1
                r+=1

            l = i
            r = i+1
            while 0 <= l and r <len(s) and s[l] == s[r]:
                if r-l+1 > len(out):
                    out = s[l:r+1]
                l-=1
                r+=1
        return out

        
        # if len(s) == 1:
        #     return s
        # out = ""
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             if len(out) < len(s[i:j+1]):
        #                 out = s[i:j+1]
        # return out
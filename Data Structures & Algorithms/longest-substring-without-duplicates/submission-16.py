class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0

        maxLen = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxLen = max(maxLen, r-l+1)

        return maxLen
            
            


        # if len(s) <= 1:
        #     return len(s)

        # word = ""
        # highest = 1
        # for i in range(len(s)):
        #     if s[i] not in word:
        #         word += s[i]
        #     else:
        #         highest = max(highest, len(word)) 
        #         while s[i] in word:
        #             word = word[1:]
        #         word += s[i]
        #     highest = max(highest, len(word))
                     

        # return highest
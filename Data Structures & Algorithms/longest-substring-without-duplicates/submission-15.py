class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        word = ""
        highest = 1
        for i in range(len(s)):
            if s[i] not in word:
                word += s[i]
            else:
                if highest < len(word):
                    highest = len(word) 
                while s[i] in word:
                    word = word[1:]
                word += s[i]
            highest = max(highest, len(word))
                     

        return highest
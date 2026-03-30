class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        charList = list(s.lower())
        for i in range(len(charList)):
            if charList[i] != charList[-1-i]:
                return False
        return True
        
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "[":"]", "{":"}"}
        stack=[]
        for c in s:
            if c in pairs:
                stack.append(c)

            else:
                try:
                    r = stack.pop()
                except:
                    return False
                if c != pairs[r]:
                    return False

        return not stack
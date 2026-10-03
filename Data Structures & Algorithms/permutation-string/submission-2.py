class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = Counter(s1)
        if len(s2) < len(s1):
            return False
        elif s1 == s2:
            return True
        else:
            match = False
            for l in range(len(s2)-len(s1)+1):
                s2Counter = Counter(s2[l:l+len(s1)])
                if s2Counter == s1Counter:
                    match = True

        return match



        



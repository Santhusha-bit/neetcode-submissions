class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(0,n+1):
            d = format(i, '032b')
            dList = list(format(i, '032b'))
            c = dList.count("1")
            out.append(c) 
        return out
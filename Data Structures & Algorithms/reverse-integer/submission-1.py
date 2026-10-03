class Solution:
    def reverse(self, x: int) -> int:
        xStrReversed = str(abs(x))[::-1]
        xInt = int(xStrReversed)

        if x < 0:
            xInt *= -1
        
        if xInt > (2 ** 31)-1 or xInt < -(2 ** 31):
            return 0
        else:
            return xInt 
        

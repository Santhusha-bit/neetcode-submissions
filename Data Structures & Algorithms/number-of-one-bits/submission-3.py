class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = list(format(n, '032b'))
        return bits.count("1")
        
        
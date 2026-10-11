class Solution:
    def reverseBits(self, n: int) -> int:
        m = "".join(list(format(n, '032b'))[::-1])
        return int(m, 2)
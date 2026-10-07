class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        k=1
        while l<r:
            k = (l+r)//2
            
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)

            if time <= h:
                r = k
            else:
                l=k+1

        return l


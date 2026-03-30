class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        if sorted(prices, reverse= True) == prices:
            return profit

        for i in range(1, len(prices)):
            s = prices[i]
            for j in range(0, i):
                b = prices[j]
                diff = s-b
                if diff > profit:
                    profit = diff
        if profit<0:
            profit=0
        return profit
        
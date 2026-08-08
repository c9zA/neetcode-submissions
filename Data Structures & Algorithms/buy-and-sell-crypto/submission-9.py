class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, lmin = 0, prices[0]
        profit = 0
        for r in range(len(prices)):
            profit = max(profit, prices[r]-lmin)
            if r>0 and prices[r-1]>prices[r]:
                l = r
                lmin = min(lmin, prices[l])
        return profit
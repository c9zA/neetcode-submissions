class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        lmin = prices[l]
        profit = 0
        for r in range(len(prices)):
            profit = max(profit, prices[r]-lmin)
            if r>0 and prices[r-1]>prices[r]:
                l = r
                lmin = min(lmin, prices[l])
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0
        if length == 2:
            return max(0, prices[1]-prices[0])
        l = 0
        lmin = prices[l]
        profit = 0
        for r in range(1,length):
            profit = max(profit, prices[r]-lmin)
            if prices[r-1]>prices[r]:
                l = r
                lmin = min(lmin, prices[l])
        return profit
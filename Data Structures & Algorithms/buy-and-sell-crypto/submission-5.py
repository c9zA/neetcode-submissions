class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0
        if length == 2:
            return max(0, prices[1]-prices[0])
        l = 0
        lmin = prices[l]
        r = 1
        profit = 0
        while r<length:
            while r+1 < length and prices[r+1]>=prices[r]:
                r += 1
            while l+1 < r and prices[l+1]<=prices[l]:
                l += 1
            lmin = min(lmin, prices[l])
            profit = max(profit, prices[r]-lmin)
            l = r
            lmin = min(lmin, prices[l])
            r += 1
        return profit
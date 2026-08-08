from math import ceil
class Solution:
    def eatTime(self, piles, k)->int:
        time = 0
        for i in range(len(piles)):
            time += ceil(piles[i]/k)
        return time
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        mn = 1
        k = 1
        while mx>=mn:
            mid = (mx+mn)>>1
            time = self.eatTime(piles, mid)
            print(mx, mn)
            print(time)
            if time<=h:
                k = mid
                mx = mid-1
            else:
                mn = mid+1
        return k
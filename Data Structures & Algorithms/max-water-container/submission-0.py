class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        l = 0
        r =length-1
        ans = 0
        while r>l:
            temp = min(heights[r], heights[l])*(r-l)
            ans = max(ans, temp)
            if heights[r]<=heights[l]:
                r-=1
            if heights[r]>heights[l]:
                l+=1
        return ans
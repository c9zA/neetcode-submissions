class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [-1]*n
        ans = 0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                idx = stack.pop()
                ans = max(ans, (i-left[idx]-1)*heights[idx])
            if stack and heights[i]==heights[stack[-1]]:
                left[i] = left[stack[-1]]
            elif stack:
                left[i] = stack[-1]
            stack.append(i)
        while stack:
            idx = stack.pop()
            ans = max(ans, (n-left[idx]-1)*heights[idx])
        return ans
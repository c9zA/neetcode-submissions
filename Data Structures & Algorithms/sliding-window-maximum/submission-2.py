import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if len(nums) == 0 or len(nums)<k:
            return ans
        window = []
        for r in range(len(nums)):
            heapq.heappush(window, (-nums[r],r))
            if r>=k-1:
                while window[0][1]<=r-k:
                    heapq.heappop(window)
                ans.append(-window[0][0])
        return ans

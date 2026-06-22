class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        ans = 0
        for n in hset:
            if n-1 not in nums:
                streak = 1
                while n+1 in nums:
                    streak += 1
                    n += 1
                ans = max(ans, streak)
        return ans
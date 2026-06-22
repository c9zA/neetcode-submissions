class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        ans = 0
        for n in nums:
            if not hmap[n]:
                hmap[n] = hmap[n-1] + hmap[n+1] + 1
                hmap[n-hmap[n-1]] = hmap[n]
                hmap[n+hmap[n+1]] = hmap[n]
                ans = max(ans, hmap[n])
        return ans
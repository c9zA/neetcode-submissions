class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set()
        seen = set()
        streak = 0
        for n in nums:
            hset.add(n)
        for n in hset:
            upper = n
            lower = n
            if n in seen:
                continue
            seen.add(n)
            while lower-1 in hset:
                lower -= 1
                seen.add(lower)
            while upper+1 in hset:
                upper += 1
                seen.add(upper)
            streak = max(streak, upper-lower+1)
        return streak
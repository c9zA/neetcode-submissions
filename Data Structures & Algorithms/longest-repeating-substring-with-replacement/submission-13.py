class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        l = 0
        ans = 0
        maxfreq = 0
        for r in range(len(s)):
            letters[s[r]] = letters.get(s[r], 0) + 1
            maxfreq = max(maxfreq, letters[s[r]])
            while r-l+1-maxfreq > k:
                letters[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
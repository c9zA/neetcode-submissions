class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = -1
        hmap = {}
        for i in range(len(s)):
            if s[i] in hmap:
                l = max(hmap[s[i]], l)
            #else:
            ans = max(ans, i-l)
            hmap[s[i]] = i
        return ans
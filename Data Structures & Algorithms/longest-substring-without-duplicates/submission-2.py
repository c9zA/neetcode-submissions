class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        letters = set()
        while r<len(s):
            if s[r] in letters:
                while l<r:
                    letters.remove(s[l])
                    if s[l] == s[r]:
                        l += 1
                        break
                    l += 1
            letters.add(s[r])
            ans = max(ans, len(letters))
            r += 1
        return ans
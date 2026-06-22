class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        l = 0
        ans = 0
        maxfreq = 0
        maxchar = ''
        for r in range(len(s)):
            letters[s[r]] = letters.get(s[r], 0) + 1
            if letters[s[r]] > maxfreq:
                maxfreq = letters[s[r]]
                maxchar = s[r]
            while r-l+1-maxfreq > k:
                letters[s[l]] -= 1
                if s[l] == maxchar:
                    m = 0
                    for ch, f in letters.items():
                        if f > m:
                            maxchar = ch
                            maxfreq = f
                            m = f
                l += 1
            print(l)
            ans = max(ans, r-l+1)
        return ans
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lens, lent = len(s), len(t)
        if lens < lent:
            return ""
        tmap = Counter(t)
        smap = {}
        unique = len(tmap)
        match = 0
        minlen = float('inf')
        ans = [-1, -1]
        l, r = -1, -1
        while l<lens:
            while r<lens:
                if match == unique:
                    break
                if r+1<lens:
                    smap[s[r+1]] = smap.get(s[r+1], 0) + 1
                    if smap[s[r+1]] == tmap.get(s[r+1], 0):
                        match += 1
                r += 1
            while l+1<lens and smap[s[l+1]]>tmap.get(s[l+1], 0):
                smap[s[l+1]] -= 1
                l += 1
            if minlen > r-l and match == unique:
                minlen = r-l
                ans[0], ans[1] = l+1, r+1
            l += 1
            if l<lens:
                if s[l] in tmap:
                    match -= 1
                smap[s[l]] -= 1
        return "" if minlen == float('inf') else s[ans[0]:ans[1]] 
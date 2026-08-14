class Solution:
    def isPalin(self, s, st, end):
        if end==st:
            return True
        for i in range(end-st+1):
            if st+i>end-i:
                break
            if s[st+i]!=s[end-i]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        ans = []
        def recurse(st):
            if st==len(s):
                ans.append(res.copy())
                return
            for end in range(st, len(s)):
                if self.isPalin(s, st, end):
                    res.append(s[st:end+1])
                    recurse(end+1)
                    res.pop()

        recurse(0)
        return ans

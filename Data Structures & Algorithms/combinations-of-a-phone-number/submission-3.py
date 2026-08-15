class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        ans = []
        chart = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        def recurse(idx):
            if idx==len(digits):
                s = "".join(res)
                ans.append(s)
                return
            digit = int(digits[idx])
            for char in chart[digit-2]:
                res.append(char)
                recurse(idx+1)
                res.pop()
        
        recurse(0)
        return ans if digits else []
        
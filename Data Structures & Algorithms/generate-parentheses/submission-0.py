class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        res = []
        def recurse(fct, bct):
            if fct>n or bct>n or fct<bct:
                return
            if len(res)==2*n:
                s = "".join(res)
                ans.append(s)
            res.append("(")
            recurse(fct+1, bct)
            res.pop()
            res.append(")")
            recurse(fct, bct+1)
            res.pop()
        recurse(0,0)
        return ans
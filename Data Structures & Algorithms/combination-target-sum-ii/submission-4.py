class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        def recurse(idx, sm, exclude):
            if sm==target:
                ans.append(res.copy())
                return
            while idx<len(candidates) and candidates[idx] in exclude:
                idx += 1
            if idx>=len(candidates) or sm>target:
                return
            res.append(candidates[idx])
            recurse(idx+1, sm+candidates[idx], exclude)
            res.pop()
            exclude.add(candidates[idx])
            recurse(idx+1, sm, exclude)
            exclude.remove(candidates[idx])
        
        recurse(0, 0, set())
        return ans

        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        candidates.sort()
        def recurse(idx, sm):
            print(res)
            if sm==target:
                ans.append(res.copy())
                return
            for i in range(idx, len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if sm+candidates[i]>target:
                    break
                res.append(candidates[i])
                recurse(i+1, sm+candidates[i])
                res.pop()
        recurse(0, 0)
        return ans

        
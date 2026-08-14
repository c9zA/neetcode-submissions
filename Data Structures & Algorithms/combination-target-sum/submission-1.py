class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        hset = set(nums)
        ans = []
        res = []
        def recurse(target, mx):
            nonlocal res
            if not hset:
                return
            if target<2:
                if target==0:
                    ans.append(res.copy())
                return
            for ele in nums:
                if ele<mx:
                    continue
                res.append(ele)
                recurse(target-ele, max(mx, ele))
                res.pop()
        recurse(target, 0)
        return ans


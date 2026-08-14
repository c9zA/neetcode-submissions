class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        def recurse(idx, sm):
            if sm==target:
                ans.append(res.copy())
            for i in range(idx, len(nums)):
                if sm+nums[i]>target:
                    continue
                res.append(nums[i])
                recurse(i, sm+nums[i])
                res.pop()
        recurse(0, 0)
        return ans
            
        

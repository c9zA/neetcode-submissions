class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        hset = set()
        res = []
        ans = []
        def recurse():
            if len(res)==len(nums):
                ans.append(res.copy())
            for num in nums:
                if num in hset:
                    continue
                res.append(num)
                hset.add(num)
                recurse()
                hset.remove(num)
                res.pop()
        recurse()
        return ans

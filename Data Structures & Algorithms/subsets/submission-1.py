class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for ct in range(2**len(nums)):
            temp = []
            for i in range(len(nums)):
                if ct&(1<<i):
                    temp.append(nums[i])
            ans.append(temp)
        return ans

        
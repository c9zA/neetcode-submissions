class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        ct = collections.Counter(nums)
        length = len(nums)
        for i in range(length):
            ct[nums[i]] -= 1
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,length):
                ct[nums[j]] -= 1
                if j-1>i and nums[j]==nums[j-1]:
                    continue
                summ = -nums[i]-nums[j]
                if ct[summ] and ct[summ]>0:
                    ans.append([nums[i], nums[j], summ])
            for j in range(i+1, length):
                ct[nums[j]] += 1
        return ans
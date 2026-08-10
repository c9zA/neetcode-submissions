class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        idx = 0
        ans = []
        while idx<len(nums)-2:
            if idx>0 and nums[idx-1]==nums[idx]:
                idx += 1
                continue
            target = -nums[idx]
            l, r = idx+1, len(nums)-1
            while r>l:
                if r<len(nums)-1 and nums[r]==nums[r+1]:
                    r-=1
                    continue
                if l>idx+1 and nums[l-1]==nums[l]:
                    l+=1
                    continue
                if nums[l]+nums[r]==target:
                    ans.append([nums[l], nums[r], nums[idx]])
                    r-=1
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    l+=1
            idx += 1
        return ans


        
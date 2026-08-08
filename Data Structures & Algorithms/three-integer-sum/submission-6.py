class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l = i+1
            r = length-1
            while r>l:
                while r>l and nums[l]+nums[r]>-nums[i]:
                    r-=1
                while r>l and nums[l]+nums[r]<-nums[i]:
                    l+=1
                if l < r and nums[l]+nums[r]==-nums[i]:
                    ans.append([nums[l], nums[r], nums[i]])
                    while l+1<r and nums[l+1]==nums[l]:
                        l+=1
                    while r-1>l and nums[r-1]==nums[r]:
                        r-=1
                    l+=1
                    r-=1
        return ans
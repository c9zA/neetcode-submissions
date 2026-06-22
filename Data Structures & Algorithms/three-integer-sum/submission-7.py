class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        for i in range(length):
            if nums[i]>0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            l = i+1
            r = length-1
            while r>l:
                if nums[r]+nums[l]>-nums[i]:
                    r-=1
                elif nums[r]+nums[l]<-nums[i]:
                    l+=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
                
        return ans
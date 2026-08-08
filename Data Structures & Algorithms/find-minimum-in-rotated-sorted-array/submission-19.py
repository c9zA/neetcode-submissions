class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        small = 0
        if r<=1:
            return min(nums)
        while r>=l:
            m = (l+r)>>1
            if nums[m-1]>=nums[m]:
                return nums[m]
            elif nums[m]>nums[r]:
                l = m+1
            else:
                r = m-1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        small = nums[0]
        while r>=l:
            m = (l+r)>>1
            if nums[m-1]>=nums[m]:
                small = nums[m]
                break
            elif nums[m]>nums[r]:
                l = m+1
            else:
                r = m-1
        return small
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)
        l = 0
        while l<r:
            m = (l+r)>>1
            if nums[m]>target:
                r=m
            else:
                l=m+1
        return l-1 if l-1>=0 and nums[l-1]==target else -1
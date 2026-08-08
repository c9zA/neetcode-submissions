class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1
        l = 0
        while l<r:
            m = (l+r)>>1
            if target<=nums[m]:
                r=m
            else:
                l = m+1
        return r if nums[r]==target else -1
from math import ceil
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        span = ceil(n/2)
        lastSpan = 10
        lastLast = lastSpan
        idx = n-1
        while span>0:
            if target<nums[idx]:
                temp = idx-span+n if idx<span else idx-span
                if nums[temp] <= nums[idx]:
                    idx = temp
            elif target>nums[idx]:
                if nums[(idx+span)%n]>=nums[idx]:
                    idx = (idx+span)%n
            else:
                return idx
            span = ceil(span/2) if lastLast!=1 else 0
            lastLast=lastSpan
            lastSpan = span
        return -1
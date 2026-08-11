class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        bucket = [0]*2001
        mx = max(nums)+1000
        for num in nums:
            bucket[num+1000]+=1
        ct = 0
        for i in range(mx, -1, -1):
            if bucket[i]==0:
                continue
            ct += bucket[i]
            if ct>=k:
                return i-1000

import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        length = len(nums)
        if length<k or length==0:
            return ans
        leftmax = []
        rightmax = [0]*length
        for i in range(length):
            if i%k==0 or leftmax[i-1]<nums[i]:
                leftmax.append(nums[i])
            else:
                leftmax.append(leftmax[i-1])
        for i in range(length-1, -1, -1):
            if i%k == k-1 or i == length-1 or rightmax[i+1]<nums[i]:
                rightmax[i] = nums[i]
            else:
                rightmax[i] = rightmax[i+1]
        print(leftmax)
        print(rightmax)
        for i in range(k, length+1):
            ans.append(max(rightmax[i-k], leftmax[i-1]))
        return ans
            
            

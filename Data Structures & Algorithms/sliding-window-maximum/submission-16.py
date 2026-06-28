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
            if i%k==0:
                leftmax.append(nums[i])
            else:
                leftmax.append(max(leftmax[i-1], nums[i]))
            if (length-1-i)%k == k-1 or i == 0:
                rightmax[length-1-i] = nums[length-1-i]
            else:
                rightmax[length-1-i] = max(rightmax[length-i], nums[length-1-i])
        print(rightmax)
        for i in range(k, length+1):
            ans.append(max(rightmax[i-k], leftmax[i-1]))
        return ans
         

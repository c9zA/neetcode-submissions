class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        right = [0]*length
        left = [0]*length
        ans = 0
        if length <= 2:
            return 0
        temp = height[0]
        for i in range(1,length):
            left[i] = max(0, temp-height[i])
            temp = max(temp, height[i])
        temp = height[-1]
        for i in range(length-1, -1, -1):
            right[i] = max(0, temp-height[i])
            temp = max(temp, height[i])
        for i in range(length):
            ans += min(left[i], right[i])
        return ans
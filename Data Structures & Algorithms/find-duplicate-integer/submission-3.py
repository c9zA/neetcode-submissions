class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)<3:
            return nums[0]
        fast = nums[0]
        slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow]==nums[fast]:
                break
        slow = nums[0]
        while True:
            if slow==fast:
                break
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
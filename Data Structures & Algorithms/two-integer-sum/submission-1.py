class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        for i in range(len(nums)):
            targetNum = target-nums[i]
            if targetNum not in hmap or hmap[targetNum]==i:
                continue
            return [i, hmap[targetNum]]
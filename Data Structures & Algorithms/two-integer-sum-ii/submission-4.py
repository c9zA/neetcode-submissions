class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while l<r:
            temp = target-numbers[l]
            if temp < numbers[l]:
                l+=1
                continue
            while temp<numbers[r]:
                r-=1
            if temp == numbers[r]:
                return [l+1, r+1]
            l+=1
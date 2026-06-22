class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length):
            temp = target-numbers[i]
            if temp<=numbers[i]:
                continue
            r = length-1
            l = i
            while r>=l:
                m = (l+r)//2
                if temp>numbers[m]:
                    l = m+1
                elif temp<numbers[m]:
                    r = m-1
                else:
                    return [i+1, m+1]
        return []
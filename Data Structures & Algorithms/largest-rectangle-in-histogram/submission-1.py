from sortedcontainers import SortedList
import bisect
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        compArr = []
        indexSort = SortedList([-1, length])
        for i in range(length):
            compArr.append((heights[i], i))
        compArr.sort()
        ans = 0
        for i in range(length):
            h, idx = compArr[i]
            start = bisect.bisect_left(indexSort, idx)
            ans = max(ans, (indexSort[start]-indexSort[start-1]-1)*h)
            indexSort.add(idx)
        return ans
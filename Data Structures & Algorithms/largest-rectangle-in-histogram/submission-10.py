sys.setrecursionlimit(200000)

class SegmentTree:
    def __init__(self, length, heights):
        self.padLen = length
        self.heights = heights
        while (self.padLen & (self.padLen-1))!=0:
            self.padLen += 1
            self.heights.append(1e9)
        self.arr = [1e9]*(self.padLen*2)
        for i in range(self.padLen, self.padLen*2):
            self.arr[i] = i-self.padLen
        idx = self.padLen*2-1
        while idx>1:
            parent = idx>>1
            self.arr[parent] = self.arr[idx] if self.heights[self.arr[idx]]<self.heights[self.arr[idx-1]] else self.arr[idx-1]
            idx -= 2
    
    def query(self, ql, qr):
        return self.queryHelper(1, 0, self.padLen-1, ql, qr)

    def queryHelper(self, node, l, r, ql, qr)->int:
        if l>qr or r<ql:
            return 1e9
        if ql<=l and qr>=r:
            return self.arr[node]
        compA = self.queryHelper(node<<1, l, (l+r)>>1, ql, qr)
        compB = self.queryHelper((node<<1)+1, ((l+r)>>1)+1, r, ql, qr)
        if compA == 1e9:
            return compB
        elif compB == 1e9:
            return compA
        else:
            return compA if self.heights[compA]<=self.heights[compB] else compB



class Solution:
    def findRecursiveArea(self, heights: List[int], ql:int, qr:int, st:SegmentTree)->int:
        if ql>qr:
            return 0
        if ql==qr:
            return heights[qr]
        minIdx = st.query(ql, qr)
        assert ql <= minIdx <= qr, f"minIdx {minIdx} out of range [{ql},{qr}]"
        ans = heights[minIdx]*(qr-ql+1)
        a = self.findRecursiveArea(heights, ql, minIdx-1, st)
        b = self.findRecursiveArea(heights, minIdx+1, qr, st)
        return max(a, b, ans)

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = SegmentTree(n, heights)
        return self.findRecursiveArea(heights, 0, n-1, st)
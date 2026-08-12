class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.count = 0
        

    def addNum(self, num: int) -> None:
        if self.count == 0:
            heapq.heappush(self.minheap, num)
        else:
            me = self.findMedian()
            if num>=me:
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
            if len(self.minheap)-len(self.maxheap)>1:
                n = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -n)
            elif len(self.maxheap)-len(self.minheap)>1:
                n = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -n)
        self.count += 1

    def findMedian(self) -> float:
        if self.count%2==0:
            return (self.minheap[0]-self.maxheap[0])/2
        if len(self.minheap)>len(self.maxheap):
            return self.minheap[0]
        return -self.maxheap[0]
        
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
        while len(heap)>1:
            big = heapq.heappop(heap)
            small = heapq.heappop(heap)
            heapq.heappush(heap, big-small)
        return -heap[0] if heap else 0
        
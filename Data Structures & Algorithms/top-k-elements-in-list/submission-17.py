import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        ct = collections.Counter(nums)
        for key, val in ct.items():
            heapq.heappush(pq, tuple([val,key]))
            if (len(pq)>k):
                heapq.heappop(pq)
        return [tup[1] for tup in pq]
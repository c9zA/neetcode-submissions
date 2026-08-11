class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        ans = []
        for i in range(len(points)):
            dist.append((math.sqrt(points[i][0]**2+points[i][1]**2), i))
        heapq.heapify(dist)
        for i in range(min(k, len(dist))):
            _, idx = heapq.heappop(dist)
            ans.append([points[idx][0], points[idx][1]])
        return ans
        
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        ma = max(ct.values())
        freq = [[] for _ in range(ma)]
        for key, val in ct.items():
            freq[val-1].append(key)
        ans = []
        for i in range(len(freq)-1, -1, -1):
            for idx in freq[i]:
                ans.append(idx)
                if len(ans)==k:
                    return ans


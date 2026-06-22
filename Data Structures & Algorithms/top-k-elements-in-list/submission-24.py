import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        ma = max(ct.values())
        freq = [[] for _ in range(ma)]
        for key, val in ct.items():
            freq[val-1].append(key)
        temp = 0
        count = -1
        ans = []
        while temp<k:
            ans.extend(freq[count])
            temp += len(freq[count])
            count -= 1
        return ans


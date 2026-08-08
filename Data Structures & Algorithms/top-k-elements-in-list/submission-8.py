class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        arr = []
        for key, val in ct.items():
            arr.append(tuple([val,key]))
        arr.sort()
        ans = []
        for i in range(k):
            ans.append(arr[-1-i][1])
        return ans
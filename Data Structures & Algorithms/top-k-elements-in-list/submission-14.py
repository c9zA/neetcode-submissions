class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        arr = []
        for key, val in ct.items():
            arr.append(tuple([val,key]))
        arr.sort()
        return [tup[1] for tup in arr[len(arr)-k:]]
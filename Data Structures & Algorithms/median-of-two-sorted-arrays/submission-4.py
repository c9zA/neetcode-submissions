import bisect
class Solution:
    def findKthSmall(self, nums1:List[int], nums2:List[int], k:int)->float:
        len1, len2 = len(nums1), len(nums2)
        if len1>len2:
            return self.findKthSmall(nums2, nums1, k)
        idx1 = min(len1, k>>1)
        idx2 = min(len2, k>>1)
        if len1==0:
            return nums2[k-1]
        if k==1:
            return min(nums1[0], nums2[0])
        if nums1[idx1-1]<=nums2[idx2-1]:
            return self.findKthSmall(nums1[idx1:], nums2, k-idx1)
        return self.findKthSmall(nums1, nums2[idx2:], k-idx2)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+ len(nums2)
        if total == 0: return 0
        if total%2!=0:
            return self.findKthSmall(nums1, nums2, (total>>1)+1)
        return (self.findKthSmall(nums1, nums2, total>>1)+self.findKthSmall(nums1, nums2, (total>>1)+1))/2
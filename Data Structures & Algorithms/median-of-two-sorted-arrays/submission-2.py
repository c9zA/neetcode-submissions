import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        total = (len1+len2)
        half = total>>1
        l2, r2 = -1, len2-1
        if len2>len1:
            return self.findMedianSortedArrays(nums2, nums1)
        while l2<=r2:
            m2=(l2+r2)>>1
            m1=half-m2-2
            comp1R = nums1[m1+1] if m1+1<len1 else float('inf')
            comp2R = nums2[m2+1] if m2+1<len2 else float('inf')
            comp1L = nums1[m1] if m1>-1 else float('-inf')
            comp2L = nums2[m2] if m2>-1 else float('-inf')
            if comp1L>comp2R:
                l2=m2+1
            elif comp2L>comp1R:
                r2=m2-1
            else:
                if total%2!=0:
                    return min(comp1R, comp2R)
                return (max(comp2L, comp1L)+min(comp2R, comp1R))/2
            
        # len1 = len(nums1)
        # len2 = len(nums2)
        # if len1==0 and len2==0:
        #     return 0
        # elif len1==0:
        #     return nums2[len2//2] if len2%2!=0 else (nums2[len2//2-1]+nums2[len2//2])/2
        # elif len2==0:
        #     return nums1[len1//2] if len1%2!=0 else (nums1[len1//2-1]+nums1[len1//2])/2

        # if len1>len2:
        #     return self.findMedianSortedArrays(nums2, nums1)
        # if len1==len2 and nums2[-1]<nums1[-1]:
        #     return self.findMedianSortedArrays(nums2, nums1)
        # lct = 0
        # l2, r2 = 0, len2-1
        # m2, idx1 = 0, 0
        # while l2<=r2:
        #     m2 = (l2+r2)>>1
        #     lct = m2
        #     idx1 = bisect.bisect_left(nums1, nums2[m2])
        #     lct += idx1
        #     if lct>(len1+len2)//2:
        #         r2=m2-1
        #     elif lct<(len1+len2)//2:
        #         l2=m2+1
        #     else:
        #         break
        # if (len1+len2)%2!=0:
        #     print('odd')
        #     return min(nums2[m2], nums1[idx1-1]) if idx1>0 else nums2[m2]
        # else:
        #     print('even1')
        #     if m2>0 and idx1>1:
        #         print(max(nums2[m2-1], nums1[idx1-2]), min(nums2[m2], nums1[idx1-1]))
        #         return (max(nums2[m2-1], nums1[idx1-2])+min(nums2[m2], nums1[idx1-1]))/2 
        #     elif m2>0 and idx1>0:
        #         return (nums2[m2-1]+nums2[m2])/2
        #     else:
        #         return (nums2[idx1-1]+min(nums2[m2], nums1[idx1-1]))/2
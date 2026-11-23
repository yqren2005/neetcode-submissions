class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        half = (len(nums1) + len(nums2)) // 2
        lo = -1 #-1 means no elements from nums1 are on the left
        hi = len(nums1) - 1
        while lo <= hi:
            m1 = (lo + hi) // 2
            m2 = half - m1 - 2
            l1 = nums1[m1] if m1 >= 0 else float('-inf')
            r1 = nums1[m1+1] if m1+1 < len(nums1) else float('inf')
            l2 = nums2[m2] if m2 >= 0 else float('-inf')
            r2 = nums2[m2+1] if m2+1 < len(nums2) else float('inf')
            if l1 <= r2 and l2 <= r1: #found partition
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(r1, r2)
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                hi = m1 - 1
            else: #l2 > r1
                lo = m1 + 1


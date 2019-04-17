'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        num3 = nums1 + nums2
        num3.sort()
        if l == 2:
            return (num3[0]+num3[1])/2
        elif l%2==0:
            return (num3[l//2-1]+num3[l//2])/2
        else:
            return num3[l//2]
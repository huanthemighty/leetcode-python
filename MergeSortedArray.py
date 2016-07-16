class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        for idx in range(n + m - 1, -1, -1):
            if i1 > -1 and i2 > -1:
                if nums1[i1] > nums2[i2]:
                    nums1[idx] = nums1[i1]
                    i1 -= 1
                else:
                    nums1[idx] = nums2[i2]
                    i2 -= 1
            elif i1 > -1:
                nums1[idx] = nums1[i1]
                i1 -= 1
            else:
                nums1[idx] = nums2[i2]
                i2 -= 1

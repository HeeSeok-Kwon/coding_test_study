class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while n > 0:
            nums1_max = 0 if m-1 < 0  else nums1[m-1]
            nums2_max = 0 if n-1 < 0  else nums2[n-1]

            if(m > 0 and nums1_max > nums2_max):
                nums1[m+n-1] = nums1_max
                m -= 1
            else:
                nums1[m+n-1] = nums2_max
                n -= 1
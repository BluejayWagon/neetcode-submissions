class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        #to perform merge sort create temp array of nums1
        nums1Temp = nums1[0:m]
        #pointer for nums1
        i = 0
        #pointer for num1Temp and nums2
        j = 0
        k = 0
        while j < m and k < n:
            if nums2[k] <= nums1Temp[j]:
                nums1[i] = nums2[k]
                k += 1
            else:
                nums1[i] = nums1Temp[j]
                j += 1 
            i += 1

        if j < m:
            for r in range(j,m):
                nums1[i] = nums1Temp[r]
                i += 1
        elif k < n:
            for r in range(k,n):
                nums1[i] = nums2[r]
                i += 1

                
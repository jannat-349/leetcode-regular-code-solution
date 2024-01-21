class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        for num in nums2:
            nums1.append(num)
        
        nums1.sort()
        m = len(nums1)
        if m % 2 == 0:
            return float(nums1[m/2] + nums1[(m-1)/2]) / 2
        else:
            return float(nums1[m/2])


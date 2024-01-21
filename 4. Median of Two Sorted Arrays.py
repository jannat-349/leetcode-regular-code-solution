class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)

        if m == 0:
            return self.findMedian(nums2)
        elif n == 0:
            return self.findMedian(nums1)

        i, j = 0, 0
        mini, prev_mini = 0, 0

        for _ in range((m + n) // 2 + 1):
            prev_mini = mini

            if i < m and (j == n or nums1[i] <= nums2[j]):
                mini = nums1[i]
                i += 1
            elif j<n and (i == m or nums1[i] >= nums2[j]):
                mini = nums2[j]
                j += 1

        if (m + n) % 2 == 0:
            return (float(prev_mini + mini) / 2)
        else:
            return float(mini)

    def findMedian(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return (float(nums[n // 2] + nums[n // 2 - 1]) / 2)
        else:
            return float(nums[n // 2])

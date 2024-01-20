class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum = 0
        n = len(arr)

        for start in range(n):
            for end in range(start + 1, n + 1):
                sorted_subList = sorted(arr[start:end])
                sum += sorted_subList[0]
        return sum % 1000000007
class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n):
            currentMax = currentSum = 0

            for j in range(i, max(-1, i-k), -1):
                if currentMax < arr[j]:
                    currentMax = arr[j]
                
                currentSumNew = currentMax * (i - j + 1) + dp[j]

                if currentSumNew > currentSum:
                    currentSum = currentSumNew
            
            dp[i + 1] = currentSum
        
        return dp[-1]
        
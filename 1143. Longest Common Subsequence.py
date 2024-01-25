class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        def lcs(x, y, m, n, memo):
            if m == 0 or n == 0:
                return 0
            elif memo[m][n] != -1:
                return memo[m][n]
            elif x[m-1] == y[n-1]:
                memo[m][n] = 1 + lcs(x, y, m-1, n-1, memo)
                return memo[m][n]
            else:
                memo[m][n] = max(lcs(x, y, m, n-1, memo), lcs(x, y, m-1, n, memo))
                return memo[m][n]
        
        m, n = len(text1), len(text2)
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        return lcs(text1, text2, m, n, memo)
        
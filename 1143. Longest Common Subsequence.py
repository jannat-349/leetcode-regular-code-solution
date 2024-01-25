class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        def lcs(x, y, m, n):
            if m == 0 or n == 0:
                return 0
            elif x[m-1] == y[n-1]:
                return 1 + lcs(x, y, m-1, n-1)
            else:
                return max(lcs(x, y, m, n-1), lcs(x, y, m-1, n))
        
        return lcs(text1, text2, len(text1), len(text2))
        
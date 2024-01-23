class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        dp = [0]
        maxLen = 0
        for word in arr:
            a, dup = 0, 0
            for alphabet in word:
                dup |= a & (1 << (ord(alphabet) - ord('a')))
                a |= 1 << (ord(alphabet) - ord('a'))
            
            if dup > 0:
                continue
            
            for i in range(len(dp) - 1, -1, -1):
                if (dp[i] & a) > 0:
                    continue
                dp.append(dp[i] | a)
                maxLen = max(maxLen, bin(dp[i] | a).count('1'))
        
        return maxLen
                    

        
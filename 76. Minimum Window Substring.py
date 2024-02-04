class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        start = end = 0
        minLen = float('inf')
        startIndex = 0
        count = len(t)

        freq = Counter(t)
        
        while end < len(s):
            if freq[s[end]] > 0:
                count -= 1
            
            freq[s[end]] -= 1
            end += 1

            while count == 0:
                if end - start < minLen:
                    minLen = end - start
                    startIndex = start

                if freq[s[start]] == 0:
                    count += 1
                freq[s[start]] += 1
                start += 1

        return "" if minLen == float('inf') else s[startIndex: startIndex + minLen]
        
class Solution(object):
    def __init__(self):
        self.count = 0

    def help(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.count += 1
            l -= 1
            r += 1

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        if n == 0:
            return 0
        
        for i in range(n):
            self.help(s, i, i)
            self.help(s, i, i + 1)
        
        return self.count
            
        
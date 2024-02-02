class Solution(object):
    
    def expand(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return s[i+1:j]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_palindrome = ''

        for i in range(len(s)):
            longest_palindrome = max(longest_palindrome, self.expand(s, i, i), self.expand(s, i, i+1), key = len)
        
        return longest_palindrome
    
    
        
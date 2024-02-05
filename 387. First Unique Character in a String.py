class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = OrderedDict(sorted(Counter(s).items(), key=lambda x: s.index(x[0])))

        unique_character = ''

        for character in freq:
            if freq[character] == 1:
                unique_character = character
                break
        
        if unique_character == '':
            return -1

        for i in range(len(s)):
            if s[i] == unique_character:
                return i
        
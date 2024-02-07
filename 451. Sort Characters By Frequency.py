class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s).most_common()
        s2 = ''
        for alphabet, count in freq:
            while count:
                s2 += alphabet
                count -= 1
        
        return s2

        
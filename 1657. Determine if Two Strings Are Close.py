class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        w1 = Counter(word1)
        w2 = Counter(word2)
        return sorted(w1.keys()) == sorted(w2.keys()) and sorted(w1.values()) == sorted(w2.values())
        
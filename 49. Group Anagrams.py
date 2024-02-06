class Solution(object):
    def getSign(self, word):
        freq = Counter(word)
        res = []
        for i in range(26):
            alphabet = chr(i + ord('a'))
            if freq[alphabet] != 0:
                res.extend([alphabet, str(freq[alphabet])])
 
        return ''.join(res)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        group = defaultdict(list)
        for word in strs:
            group[self.getSign(word)].append(word)
        
        res.extend(group.values())
        return res
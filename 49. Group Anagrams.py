class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for word in strs:
            res.setdefault(''.join(sorted(word)), []).append(word)
        
        return res.values()
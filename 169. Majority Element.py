class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        n = len(nums)

        for key in freq:
            if freq[key] > n / 2:
                return key
                
        
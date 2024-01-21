class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        norob = 0

        for num in nums:
            rob2 = norob + num
            norob2 = max(rob, norob)
            rob = rob2
            norob = norob2
        
        return max(rob, norob)
        
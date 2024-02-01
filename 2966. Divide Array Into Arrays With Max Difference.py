class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        
        nums.sort()

        answer = []

        for i in range(0, n, 3):
            if i + 2 < n and nums[i+2] - nums[i] <= k:
                answer.append([nums[i], nums[i+1], nums[i+2]])
            else:
                return []
        
        return answer
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]

        for i in range(3, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
        
        return max(dp)
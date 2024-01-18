class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        paths= [0]*(n+1)
        paths[0] = 1
        paths[1] = 2
        for i in range(2,n):
            paths[i] = paths[i-1]+paths[i-2]

        return paths[n-1]

        
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]

        cherries = 0
        dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]

        for i in range(1, rows):
            for j in range(cols):
                for k in range(cols):
                    if j > i or k < cols - i - 1 or j > k:
                        continue
                    
                    dp[i][j][k] = dp[i - 1][j][k]

                    if j - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k])
                    if j - 1 >= 0 and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1])
                    if j - 1 >= 0 and k + 1 < cols:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k + 1])
                    if j + 1 < cols:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k])
                    if j + 1 < cols and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k - 1])
                    if j + 1 < cols and k + 1 < cols:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k + 1])
                    if k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
                    if k + 1 < cols:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k + 1])
                    if j != k:
                        dp[i][j][k] += grid[i][j] + grid[i][k]
                    else:
                        dp[i][j][k] += grid[i][j]

                    cherries = max(cherries, dp[i][j][k])

        return cherries


        
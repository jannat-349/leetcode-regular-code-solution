class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 1000000000 + 7
        paths = [[0] * n for _ in range(m)]
        paths[startRow][startColumn] = 1
        count = 0

        for moves in range(1, maxMove + 1):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + paths[i][j]) % MOD
                    if j == n - 1:
                        count = (count + paths[i][j]) % MOD
                    if i == 0:
                        count = (count + paths[i][j]) % MOD
                    if j == 0:
                        count = (count + paths[i][j]) % MOD
                    
                    temp[i][j] = (
                        ((paths[i-1][j] if i > 0 else 0) + (paths[i+1][j] if i < m-1 else 0)) % MOD + 
                        ((paths[i][j-1] if j > 0 else 0) + (paths[i][j+1] if j < n-1 else 0)) % MOD
                    ) % MOD

            paths = temp
        
        return count

        
        
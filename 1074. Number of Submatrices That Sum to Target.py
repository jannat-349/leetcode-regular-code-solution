class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """

        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(1, n):
                matrix[row][col] += matrix[row][col-1]
        
        count = 0

        for val1 in range(n):
            for val2 in range(val1, n):
                prefix_sum = {0:1}
                sum = 0

                for row in range(m):
                    sum += matrix[row][val2] - (matrix[row][val1 - 1] if val1 > 0 else 0)
                    count += prefix_sum.get(sum - target, 0)
                    prefix_sum[sum] = prefix_sum.get(sum, 0) + 1
        
        return count
        
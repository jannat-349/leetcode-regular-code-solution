class Solution(object):

    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum = 0
        MOD = 10**9+7
        stack = []
        n = len(arr)

        for i in range(n+1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                count = (mid-left) * (right-mid) % MOD
                sum += (count * arr[mid]) % MOD
                sum %= MOD
            stack.append(i)

        return sum

        
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """

        ans = [0] * n
        times = [0] * n
        meetings.sort()

        for start, end in meetings:
            flag = False
            minIndex = -1
            val = float('inf')

            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minIndex = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break

            if not flag:
                ans[minIndex] += 1
                times[minIndex] += (end - start)

        maxi = -1
        id = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i
        return id

        
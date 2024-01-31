class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        deq = deque()
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)-1, -1, -1):
            if not deq:
                deq.appendleft(i)
                answer[i] = 0
            else:
                while deq and temperatures[i] >= temperatures[deq[0]]:
                    deq.popleft()
                if not deq:
                    answer[i] = 0
                else:
                    answer[i] = deq[0] - i
                
                deq.appendleft(i)
        
        return answer
        
        


        
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        answer = []

        for i in range(1, 10):
            num = i
            next_num = i + 1

            while num <= high and next_num <= 9:
                num = num * 10 + next_num

                if low <= num <= high:
                    answer.append(num)
                next_num += 1
        

        answer.sort()
        return answer

        
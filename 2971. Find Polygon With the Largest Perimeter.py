class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        perimeter = -1
        for num in nums:
            if num < sum:
                perimeter = num + sum
            
            sum += num
        
        return perimeter
                

        
        


        
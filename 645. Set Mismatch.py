class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        first = 0
        second = len(nums)
        
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                first = nums[i]

        nums2 = list(set(nums))

        for i in range(0, len(nums2)):
            if nums2[i] != i+1:
                second = i+1
                break

        # print(nums)
        

        return[first,second]

        
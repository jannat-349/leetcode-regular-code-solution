class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def getUniqueStringLen(index, visited):
            if index >= len(arr):
                return 0
            
            maxLen = 0
            isPossible = True
            duplicate = set()

            for alphabet in arr[index]:
                if alphabet in visited or alphabet in duplicate:
                    isPossible = False
                    break
                duplicate.add(alphabet)
                
            add, noAdd = 0, 0
            if isPossible:
                for alphabet in arr[index]:
                    visited.add(alphabet)
                add = len(arr[index]) + getUniqueStringLen(index+1, visited)
                for alphabet in arr[index]:
                    visited.remove(alphabet)
            noAdd = getUniqueStringLen(index+1, visited)
            maxLen += max(add, noAdd)
            return maxLen
        
        visited = set()
        return getUniqueStringLen(0, visited)
                    
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq = Counter(arr)
        items_list = list(freq.items())
        for item in sorted(items_list, key=lambda x: x[1]):
            if k <= 0:
                break

            key, value = item
            if value <= k:
                k -= value
                print(freq[key])
                del freq[key]
                
        return len(freq)
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        mat2 = list(mat)
        mat2.sort()
        ans = []


        for i in range(k):
            for j in range(len(mat)):
                if mat2[i] == mat[j] and mat[j] != [-1]:
                    ans.append(j)
                    mat[j] = [-1]
                    break
        
        return ans
        



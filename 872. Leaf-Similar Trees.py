# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverseTree(self, root):
        res = []
        if root.left == None and root.right == None:
            return [root.val]
        if root.left:
            res.extend(self.traverseTree(root.left))
        if root.right:
            res.extend(self.traverseTree(root.right))

        print(res)
        return res


    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.traverseTree(root1) == self.traverseTree(root2)

            

        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        valList = []

        def bianLi(root):
            if root == None:
                return
            valList.append(root.val)
            if root.left:
                bianLi(root.left)
            if root.right:
                bianLi(root.right)
        
        bianLi(root)
        return valList

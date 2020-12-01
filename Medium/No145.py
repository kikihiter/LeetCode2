# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        valList = [] # 用来存储遍历过程中的值
        # 遍历
        def bianLi(root):
            if root == None:
                return
            bianLi(root.left)
            bianLi(root.right)
            valList.append(root.val)
        bianLi(root)
        return valList
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        if len(inorder) == len(postorder) == 1:
            return TreeNode(postorder[-1])
        nodeVal = postorder[-1]
        i = inorder.index(nodeVal)
        root = TreeNode(nodeVal)
        if i > 0 :
            root.left = self.buildTree(inorder[:i], postorder[:i])
        if i < len(postorder)-1:
            root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
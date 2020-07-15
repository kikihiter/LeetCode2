# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        if len(preorder) == len(inorder) == 1:
            return TreeNode(inorder[0])
        nodeVal = preorder[0]
        root = TreeNode(nodeVal)
        i = inorder.index(nodeVal)
        if i > 0:
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        if i < len(preorder) - 1:
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root

        
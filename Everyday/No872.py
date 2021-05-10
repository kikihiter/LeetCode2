# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        """
        210510
        求叶子节点
        """
        def leaf(root):
            stack = []
            ans = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if not root.right and not root.left:
                    ans.append(root.val)
                root = root.right
            return ans
        
        
        leafList1 = leaf(root1)
        leafList2 = leaf(root2)
        if len(leafList1) != len(leafList2):
            return False
        for i in range(len(leafList1)):
            if leafList1[i] != leafList2[i]:
                return False
        return True
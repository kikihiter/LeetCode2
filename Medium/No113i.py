# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            if sum == root.val:
                sumList = root.val
                return [[root.val]]
            else:
                return[]
        pathAll = []
        if root.left:
            pathLeft = self.pathSum(root.left, sum-root.val)
            pathAll.extend(pathLeft)
        if root.right:
            pathRight = self.pathSum(root.right, sum-root.val)
            pathAll.extend(pathRight)
            
        if not pathAll:
            return []
        for path in pathAll:
            path.insert(0, root.val)
        return pathAll
        
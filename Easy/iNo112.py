class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        if self.hasPathSum(root.left, sum - root.val) == True or self.hasPathSum(root.right, sum - root.val) == True:
            return True
        return False
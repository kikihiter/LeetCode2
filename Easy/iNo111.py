class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l == 0:
            return r + 1
        if r == 0:
            return l + 1
        return min(l, r) + 1
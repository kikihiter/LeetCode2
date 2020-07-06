class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def h(node):
            """
            type: TreeNode
            rtype: tuple(int, bool)
            tup(height, if balance)
            """
            if node == None:
                return (0, True)
            l1, l2 = h(node.left)
            r1, r2 = h(node.right)
            if l2 == False or r2 == False:
                return (0, False)
            if abs(l1-r1) > 1:
                return (0, False) 
            height = max(l1,r1) + 1
            return (height, True)

        return h(root)[1]
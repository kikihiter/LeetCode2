class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def nodeValue(m, n):
            """
            :type m n: int
            :rtype: TreeNode
            """
            if m == n:
                return TreeNode(nums[m])
            if n-m == 1:
                node = TreeNode(nums[m])
                node.right = TreeNode(nums[n])
                return node
            node = TreeNode(nums[m + (n-m)/2])
            node.left = nodeValue(m, m + (n-m)/2 - 1)
            node.right = nodeValue(m + (n-m)/2 + 1, n)
            return node
        
        l = len(nums)
        if l > 0:
            return nodeValue(0, l-1)
        else:
            return None
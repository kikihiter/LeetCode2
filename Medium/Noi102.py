# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodeList = []
        i = 0
        
        def deep(node, h):
            if node:
                nodeList.append((node, h))
                if node.left:
                    deep(node.left, h+1)
                if node.right:
                    deep(node.right, h+1)

        deep(root, i)
        
        ans = []
        for tup in nodeList:
            node, h = tup
            if h >= len(ans):
                ans.append([])
            ans[h].append(node.val)
        return ans

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        用一个栈来记录遍历进度，栈中元素（root, h）,root为当前节点，h为当前节点深度
        """
        if not root:
            return []
        nodeStack = [(root, 0)]
        ans = []
        while nodeStack != []:
            node, h = nodeStack.pop(-1)
            if h > len(ans)-1:
                ans.append(node.val)
            if node.left:
                nodeStack.append((node.left, h+1))
            if node.right:
                nodeStack.append((node.right, h+1))
        return ans
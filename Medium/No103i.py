# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        isLeft = True
        queue = [root]
        ans = []
        while queue:
            temp = []
            size = len(queue)
            for node in range(size):
                node1 = queue.pop(0)
                temp.append(node1.val)
                if node1.left:
                    queue.append(node1.left)
                if node1.right:
                    queue.append(node1.right)
            if isLeft == True:
                ans.append(temp)
                isLeft = False
            else:
                ans.append(temp[::-1])
                isLeft = True
        return ans

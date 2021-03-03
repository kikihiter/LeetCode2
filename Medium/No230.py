# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        """
        想复杂了
        不断把左子节点入栈
        """
        stack = [root]
        # 用来处理二叉树的栈
        ans = []    # 最小的数的集合
        while stack != []:
        # 栈中还有节点
            while root and root.left:
            # 找到最左下角的子节点，并入栈
                root = root.left
                stack.append(root)
            root = stack.pop(-1)
            # 取出一个栈中节点
            ans.append(root.val)
            # 读取他的值
            if len(ans) == k:
                print ans
                return ans[-1]
            if root.right:
            # 如果当前节点有右子节点，则右移
                root = root.right
                stack.append(root)
            else:
                root = None
        return ans[-1]
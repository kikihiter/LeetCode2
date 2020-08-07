# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        """
        # 运用栈存储右子树，不断向下遍历二叉树，严格来说，不是in place，但是通过了检测
        rightNodeList = []
        while root:
            if not root.left and not root.right:
                if len(rightNodeList) == 0:
                    break
                else:
                    root.right = rightNodeList.pop(-1)
                    root = root.right
            if root.left and not root.right:
                root.right = root.left
                root.left = None
                root = root.right
            if not root.left and root.right:
                root = root.right
                continue
            if root.left and root.right:
                rightNodeList.append(root.right)
                root.right = root.left
                root.left = None
                root = root.right
        """
        # 看了一下标准答案的思想，寻找右子节点的前驱节点（也就是左子树的前序遍历的最后一个节点），自己来实现一下
        while root:     # 边界条件，当节点存在时
            if root.left:   # 如果有左子节点
                rootPre = rootFlag = root.left # 寻找前驱结点
                while rootFlag: # 用一个rootFlag来判断前驱节点是否是子节点的最后一个节点，当flag存在时，则仍有可能不是最后一个
                    rootPre = rootFlag
                    while rootPre.right:
                        rootPre = rootPre.right
                    rootFlag = rootPre.left # rootFlag左移，判断rootPre是否有左子节点
                temp = root.right   # 用temp记录下右子节点
                root.right = root.left
                root.left = None
                rootPre.right = temp
            root = root.right   # 节点不断右移

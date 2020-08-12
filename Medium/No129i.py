# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 不存在时，返回0
        if not root:
            return 0
        nodeQueue = [root]  # 处理节点的队列
        valQueue = [root.val]   # 将数值存储在此队列中
        sumVal = 0    # 每到达一个叶子节点，计算一次数字和
        # 当队列不为空（即未遍历完时）
        while nodeQueue != []:
            node = nodeQueue.pop(0)
            val = valQueue.pop(0)
            # 左子节点存在时
            if node.left:
                nodeQueue.append(node.left)
                valQueue.append(val*10+node.left.val)
            # 右子节点存在时
            if node.right:
                nodeQueue.append(node.right)
                valQueue.append(val*10+node.right.val)
            # 无子节点，即此节点为叶子节点，进行数字和计算
            if not node.left and not node.right:
                sumVal += val
        return sumVal
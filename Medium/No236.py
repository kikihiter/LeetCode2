# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        用一个列表来存储任意节点的路径
        其中0代表左边，1代表右边
        """
        stack = [(root,[])]
        x1 = None
        x2 = None
        while stack != []:
        # 还有未处理的节点
            iNode, iPass = stack.pop(-1)
            # print iNode.val, iPass
            if iNode.val == p.val:
            # 找到了p节点
                print "hello", iPass
                x1 = iPass
            if iNode.val == q.val:
            # 找到了q节点
                x2 = iPass
            if x1 and x2:
            # 两个节点都已经找到了
                break
            if iNode.left:
                stack.append((iNode.left,iPass+[0]))
            if iNode.right:
                stack.append((iNode.right,iPass+[1]))
        print x1,x2
        if x1 == [] or x2 == []:
        # 有一个是根节点
            return root
        for i in range(min(len(x1),len(x2))):
            if x1[i] != x2[i]:
                break
            if x1[i] == 0:
                root = root.left
            elif x1[i] == 1:
                root = root.right
        return root
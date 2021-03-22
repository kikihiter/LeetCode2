# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        210322
        """
        # # 根节点为空，返回True
        # if not root:
        #     return True
        # # 左右两节点为空，返回True
        # if not root.left and not root.right:
        #     return True
        # # 没有左子树
        # if not root.left:
        #     # 右子树节点较小，不正确
        #     if root.val >= root.right.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.right)
        # # 没有右子树
        # if not root.right:
        #     # 左子树较大，不正确
        #     if root.left.val >= root.val:
        #         return False
        #     else:
        #         return self.isValidBST(root.left)
        # # 左根右符合要求，判断他们的子树
        # if root.left.val <= root.val <= root.right.val:
        #     return self.isValidBST(root.left) and self.isValidBST(root.right)
        # # 不符合要求，返回False
        # return False
        
        # """
        # 先获取前序遍历序列，再根据序列判断
        # """
        # # 前序遍历
        # def qianXu(root):
        #     if not root:
        #         return
        #     qxList.append(root.val)
        #     if root.left:
        #         qianXu(root.left)
        #     if root.right:
        #         qianXu(root.right)

        # def isBalance(iList):
        #     if not iList or len(iList)<2:
        #         return True
        #     i = 1
        #     rootVal = iList[0]
        #     lList, rList = [], []
        #     while i < len(iList):
        #         if rootVal == iList[i]:
        #             return False
        #         elif rootVal < iList[i]:
        #             break
        #         lList.append(iList[i])
        #         i += 1
        #     while i < len(iList):
        #         if rootVal >= iList[i]:
        #             return False
        #         else:
        #             rList.append(iList[i])
        #         i += 1
        #     return isBalance(lList) and isBalance(rList)

        # qxList = []
        
        # qianXu(root)
        # print qxList
        # return isBalance(qxList)


        """
        傻逼了，这么简单的题，搞得这么复杂，直接判断中序遍历是否升序就行了
        用递归太简单了，写个循环练练手
        """
        # 根节点不存在，直接返回
        if not root:
            return True
        
        stack = [root]  # 用于存储节点
        mark = []   # 用来标记已经遍历过的点
        haveFir = False  # 用来第一个节点是否已经被处理了，起始标记为False
        # 不为空，仍有节点未遍历
        while stack != []:
            node = stack.pop()
            # 不存在左节点或者左节点已经遍历过的时候，遍历当前节点
            if not node.left or node.left in mark:
                # 比较当前节点与上个节点的数值，若符合要求，则将当前节点数值赋给preVal
                if haveFir == False:
                    haveFir = True
                    preVal = node.val
                else:
                    if preVal >= node.val:
                        return False
                    preVal = node.val
                mark.append(node)   # 标记此点已经遍历过了
                # 将未处理过的右子树存入栈中
                if node.right and node.right not in mark:
                    stack.append(node.right)
            # 存在左子节点时，将本节点和左子节点共同入栈，等待后续处理
            else:
                stack.append(node)
                stack.append(node.left)
        return True
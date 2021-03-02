# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        对于第h层，元素个数在1与2的h-1方个元素之间，且每个节点可以用h-1位二进制表示（0代表左节点，1代表右节点）
        首先通过对左子节点不断递进得到二叉树深度H
        数出二叉树第H层节点个数即可知道总节点个数
        假设第H层满编，给其中所有节点用二进制编码，编码代表的数字为0到2的h-1方减一，用二分法找到不存在的点中最靠左的点，即可判断出个数
        """
        def haveNode(num, h):
        # 判断h层数字num代表的节点是否存在
            temp = root
            for i in range(h-2, -1, -1):
                j = (num>>i) & 1
                if j == 0:
                    if temp.left == None:
                        return False
                    temp = temp.left
                else:
                    if temp.right == None:
                        return False
                    temp = temp.right
            return True
        
        if root == None:
            return 0
        leftNode = root
        h = 1
        while leftNode.left:
            h += 1
            leftNode = leftNode.left
        # 得出二叉树深度h

        left, right, maxN = 0, (1<<(h-1))-1, (1<<(h-1))-1
        while 0 <= left <= right <= maxN:
            middle = (left+right)>>1
            # print left,middle,right,h,haveNode(middle, h)
            if haveNode(middle, h) == True:
                left = middle + 1
            else:
                right = middle
            if left == right:
                if haveNode(left, h) == True:
                # 全满了
                    left += 1
                break
        # print h, left
        return (1<<(h-1)) + left -1



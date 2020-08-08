"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        """
        # 主体思路思路和上一题（116）相似，经过上题实际操作发现，并不需要将每一层的节点都进行保存，实际上只需要保存当前层和下一层的节点
        """
        # 为空时直接返回
        if not root:
            return
        level = [root]  # 用于存储当前层的节点，初始化
        levelNext = []

        # 未处理至最后一层
        while level != []: 
            # 提出当前层第一个节点
            temp = level.pop(0)
            # 存储它的子节点信息至下一层
            if temp.left:
                levelNext.append(temp.left)
            if temp.right:
                levelNext.append(temp.right)
            
            # 当前层仍有节点未处理时
            while level != []:
                temp.next = level.pop(0)
                temp = temp.next
                if temp.left:
                    levelNext.append(temp.left)
                if temp.right:
                    levelNext.append(temp.right)
            level = levelNext
            levelNext = []
        return root

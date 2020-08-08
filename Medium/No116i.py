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
        if not root:
            return
        level = []  # 将每一层的节点分别存储在level中，每有一层，level增加一个空列表作为元素
        temp = root
        while temp:
            level.append([])
            temp = temp.right
        level[0].append(root)   # 将根节点添加到层列表中
        for i in range(len(level)):
            temp = level[i].pop(0)
            # 取出本层列表的第一个节点
            if temp.left:
                level[i+1].extend([temp.left, temp.right])
            # 如果不是最后一层的话，将其子节点分别添加到下层列表中

            while level[i] != []:
            # 当本层仍有节点未被处理时
                temp.next = level[i].pop(0)
                # 取出下一节点
                temp = temp.next
                if temp.left:
                    level[i+1].extend([temp.left, temp.right])
        return root


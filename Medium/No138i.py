"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        """
        第一遍遍历链表，每遍历一个节点，新创建一个节点，赋值，同时用两个列表分别存入新旧两个节点
        第二遍遍历链表，观察random信息，从列表1中返回序号，根据序号从列表2中找出节点，建立联系
        """
        # 为空
        if not head:
            return
        oldList = [head]    # 旧节点列表
        headNew = Node(head.val)    # 新链表头
        newList = [headNew] # 新节点列表
        temp = head.next # 临时节点
        # 不为空时，遍历链表
        while temp:
            nodeNew = Node(temp.val)
            nodeOld = newList[-1]
            nodeOld.next = nodeNew
            oldList.append(temp)
            newList.append(nodeNew)
            temp = temp.next
        temp = head
        # 遍历链表，并用i记录深度
        for i in range(len(newList)):
            # 当当前节点没有random时，直接跳过
            if not temp.random:
                temp = temp.next
                continue
            j = oldList.index(temp.random)
            newList[i].random = newList[j]
            temp = temp.next
        return newList[0]

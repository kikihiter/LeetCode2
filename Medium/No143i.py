# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodeList = []   # 用于存储读取到的节点
        temp = head
        # 遍历节点并断开
        while temp != None:
            nextNode = temp.next
            temp.next = None
            nodeList.append(temp)
            temp = nextNode
        beforeNode = ListNode() # 用于存储上一个节点的信息
        while nodeList != []:
            nowNode = nodeList.pop(0)
            if nodeList == []:  # 如果列表为空 
                beforeNode.next = nowNode
                break
            nextNode = nodeList.pop(-1)
            beforeNode.next = nowNode
            nowNode.next = nextNode
            beforeNode = nextNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = None # 空，用来存储上一个节点信息
        while head != None:
            nextNode = head.next
            head.next = temp
            temp = head
            head = nextNode
        return temp
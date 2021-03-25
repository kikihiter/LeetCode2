# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        210325
        让一个指针先走n步，然后另一个指针开始走，第一个指针走到结尾的时候，另一个指针即是要求删除的点
        注意边界条件
        """
        head = ListNode(None, head)
        fast = head
        while fast.next:
            fast = fast.next
            n -= 1
            if n == 0:
                break
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head.next
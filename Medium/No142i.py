# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        用快慢指针的思路来解题，每次慢指针走一格，快指针走两格。
        整个链表分为两部分，直线的部分和环的部分。
        """
        # 不存在链表时直接返回None
        if not head:
            return None
        slow = fast = head.next    # 慢指针
        if slow:       
            fast = slow.next    # 快指针
        if not fast:
            return None
        # 当没有遍历完时
        while fast:
            # 两指针相遇
            if fast == slow:
                break
            # 遍历到尽头，证明没有环，返回None
            if not fast.next:
                return None
            slow = slow.next    # 慢指针移动一格
            fast = fast.next    # 快指针移动一格
            if not fast.next:
                return None
            fast = fast.next    # 快指针再移动一格
        
        # 有环，则必相遇
        while 1:
            # 相遇，此点为链表入环点
            if head == fast:
                return head
            head = head.next
            fast = fast.next
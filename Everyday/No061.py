# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """
        210327
        将尾结点连接到第一个节点，并把倒数第k个节点后面断掉即可
        关键在于找到第k节点
        应当注意k的值大于链表长度的情况
        """
        if not head:
            return head
        l = 0
        root = head
        while l < k and root.next:
            root = root.next
            l += 1
        
        if l < k:
            k = k%(l+1)
            root.next = head
            root = root.next
            while k<l:
                root = root.next
                k += 1
            head = root.next
            root.next = None
            return head
        else:
            slow = head
            while root.next:
                slow = slow.next
                root = root.next
            root.next = head
            head = slow.next
            slow.next = None
            return head
            
            
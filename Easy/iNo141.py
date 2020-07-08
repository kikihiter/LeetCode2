# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        nodeSet = set()
        while 1:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            if head.next:
                head = head.next
            else:
                return False
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ha, hb = headA, headB 
        h1, h2 = 0, 0
        while ha != None:
            if not ha.next:
                break
            ha = ha.next
            h1 += 1
        while hb != None:
            if not hb.next:
                break
            hb = hb.next
            h2 += 1
        if ha != hb:
            print "here"
            return None
        ha, hb = headA, headB
        if h1 > h2:
            while h1 != h2:
                ha = ha.next
                h1 -= 1
        else:
            while h1 != h2:
                hb = hb.next
                h2 -= 1
        while ha and hb:
            if ha == hb:
                return ha
            ha = ha.next
            hb = hb.next

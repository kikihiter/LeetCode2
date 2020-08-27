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
        if not head:
            return head
        p=head
        while p:
            tmp=p.next
            clone=Node(p.val,p.next,None)
            p.next=clone
            p=tmp
        p=head
        while p:
            if p.random:
                p.next.random=p.random.next
            p=p.next.next
        clonehead=head.next
        p=head
        q=clonehead
        while p:
            p.next=p.next.next
            q.next=q.next.next if q.next else None
            p=p.next
            q=q.next
        return clonehead


"""
答案里用时最短的一个，看了一下，挺巧妙的，感觉是标准答案。
一共有3个while，整个代码也分为这三个主要部分
原链表结构：O1->O2->O3
第一个，在原链表上创建新的克隆节点，使节点变为：O1->N1->O2->N2->O3->N3
第二个，建立random关系
第三个，断开两个链表，变为：O1->O2->O3和N1->N2->N3
"""
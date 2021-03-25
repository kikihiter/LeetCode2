# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        用一个栈stack存储遍历过的节点，用一个数字记录上一个节点的值preVal
        每遇到一个新的节点，与preVal比较，如果相同，跳过；如果不同，入栈
        每次更新preVal值
        210325
        """
        stack = []  # 记录节点值
        root = head 
        preVal = None   # 记录上一个节点数值
        while root:
            # 当前节点与上个节点数值相同，且上一个节点仍在栈中时，将上一个节点弹出
            if root.val == preVal and stack != [] and stack[-1].val == preVal:
                    stack.pop(-1)
            # 当前节点与上个节点数值不同，入栈
            elif root.val != preVal:
                # 栈为空时，直接入栈
                if stack == []:
                    stack.append(root)
                    preVal = root.val
                # 栈不为空时，与栈中最后一个元素建立联系
                else:
                    preNode = stack[-1]
                    preNode.next = root
                    preVal = root.val
                    stack.append(root)
            root = root.next
        # 栈不为空，即原链表中存在不重复的元素
        if stack != []:
            # 将最后一个节点指向None，返回第一个不重复的节点
            stack[-1].next = None
            return stack[0]
        # 栈为空时，证明原链表全部为重复数字，或者干脆为空，直接返回空
        return
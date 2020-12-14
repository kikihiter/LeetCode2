# 很简单的一道题，我怎么就写不了这么简洁，最后还超时了。。。
# 这里精妙的地方有两点：1.哑指针作为头指针，方便将节点插入在头指针之前；2.设立了一个lastSorted用来记录排完序的最后一个节点，需要注意的是，排序过程中此节点后面跟着后序节点
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next
        
        return dummyHead.next

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/insertion-sort-list/solution/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
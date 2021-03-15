"""
少打一个next，害得我debug了好久
21/03/13
"""
class Node(object):
# 链表节点
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 769
        # 分桶数设置位769
        self.keyList = [0]*self.base
        # 生成一个长度为base的数组

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % self.base
        # key映射为索引
        nodeA = Node(key)
        # 新的节点
        if self.keyList[i] == 0:
        # 数组中此位置还没有节点
            self.keyList[i] = nodeA
        else:
            root = self.keyList[i]
            if root.val != key:
            # 初始节点不为key
                while root.next:
                    root = root.next
                    if root.val == key:
                    # 如果链表中存在key，什么也不做，直接跳出循环
                        break
                else:
                # 循环正常结束，证明链表中不存在key
                    root.next = nodeA
                    # 在链表最后添加节点

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = key % self.base
        if self.keyList[i] != 0:
        # 为0时证明key根本不在，不用考虑，所以只考虑不为0时的
            root = self.keyList[i]
            # 根节点
            if root.val == key:
            # 第一个点就是目标点
                if root.next:
                # 如果存在下一个节点，将keyList直接链接到下一个点上
                    self.keyList[i] = root.next
                else:
                # 不存在下一个节点，即这个链表只有目标点时，重置链表
                    self.keyList[i] = 0
            else:
                while root.next:
                    if root.next.val == key:
                    # 找到目标点
                        root.next = root.next.next
                        break
                    root = root.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        i = key % self.base
        if self.keyList[i] == 0:
            return False
        root = self.keyList[i]
        while root:
            if root.val == key:
                return True
            root = root.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
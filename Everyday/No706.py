"""
改的昨天的题
21/03/14
"""
class Node(object):
# 链表节点
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 769
        # 分桶数设置位769
        self.keyList = [0]*self.base
        # 生成一个长度为base的数组

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        i = key % self.base
        # key映射为索引
        nodeA = Node(key, value)
        # 新的节点
        if self.keyList[i] == 0:
        # 数组中此位置还没有节点
            self.keyList[i] = nodeA
        else:
            root = self.keyList[i]
            if root.key != key:
            # 初始节点不为key
                while root.next:
                    root = root.next
                    if root.key == key:
                    # 如果链表中存在key
                        root.value = value
                        break
                else:
                # 循环正常结束，证明链表中不存在key
                    root.next = nodeA
                    # 在链表最后添加节点
            else:
            # 初始节点是目标点
                root.value = value



    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        i = key % self.base
        # key映射为索引
        if self.keyList[i] == 0:
        # 数组中此位置还没有节点
            return -1
        else:
            root = self.keyList[i]
            if root.key != key:
            # 初始节点不为key
                while root.next:
                    root = root.next
                    if root.key == key:
                    # 如果链表中存在key
                        return root.value
                else:
                # 循环正常结束，证明链表中不存在key
                    return -1
            else:
            # 初始节点是目标点
                return root.value

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        i = key % self.base
        if self.keyList[i] != 0:
        # 为0时证明key根本不在，不用考虑，所以只考虑不为0时的
            root = self.keyList[i]
            # 根节点
            if root.key == key:
            # 第一个点就是目标点
                if root.next:
                # 如果存在下一个节点，将keyList直接链接到下一个点上
                    self.keyList[i] = root.next
                else:
                # 不存在下一个节点，即这个链表只有目标点时，重置链表
                    self.keyList[i] = 0
            else:
                while root.next:
                    if root.next.key == key:
                    # 找到目标点
                        root.next = root.next.next
                        break
                    root = root.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
class LRUCache(object):
    """
    用两个列表实现，每次存取时，将处理过的元素后置。将要超出容量时，抛出第一个元素。
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.iKey = []  # 用于存储key
        self.iValue = []    # 用于存储value


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 如果key已经存在
        if key in self.iKey:
            iIndex = self.iKey.index(key)
            newKey = self.iKey.pop(iIndex)
            # 将其从原本位置抛出，并添加到列表末尾
            self.iKey.append(newKey)
            newValue = self.iValue.pop(iIndex)
            self.iValue.append(newValue)
            return newValue
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 如果已经存在
        if key in self.iKey:
            iIndex = self.iKey.index(key)
            # 读取对应索引
            self.iKey.pop(iIndex)
            self.iKey.append(key)
            self.iValue.pop(iIndex)
            self.iValue.append(value)
        else:
            # 达到容量上限时，抛出最远时间的缓存
            if len(self.iKey) == self.capacity:
                self.iKey.pop(0)
                self.iValue.pop(0)  
            self.iKey.append(key)
            self.iValue.append(value)
            # 将新的缓存存入末尾

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
"""
210323
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # 初始化的时候，把所有元素按顺序存入iList中
        self.iList = []
        self.i = -1
        nestedList = nestedList[::-1]
        # 当nesterList不为空，也就是还有元素没有录入完成时
        while nestedList != []:
            # 取出最后一位
            nested = nestedList.pop()
            # 如果最后一位为整型，读取并录入iList中，否则，将其逆序放入栈中（为保证顺序，使前面的数字最先处理，需要逆序入栈）
            if nested.isInteger() == True:
                self.iList.append(nested.getInteger())
            else:
                for nest in nested.getList()[::-1]:
                    nestedList.append(nest)

        

    def next(self):
        """
        :rtype: int
        """
        # 利用索引值直接读取对应元素
        self.i += 1
        if self.i < len(self.iList):
            return self.iList[self.i]

    def hasNext(self):
        """
        :rtype: bool
        """
        # 当索引值达到最后一个元素时，不存在下一个元素了，返回False，其余时候返回True
        if self.i >= len(self.iList)-1:
            return False
        return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
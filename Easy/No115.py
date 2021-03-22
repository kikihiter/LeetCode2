class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minData = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.minData == []:
            self.minData.append(x)
        else:
            y = self.minData[-1]
            if y <= x:
                self.minData.append(y)
            else:
                self.minData.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack == []:
            return
        self.minData.pop(-1)
        return self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if self.stack == []:
            return
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minData == []:
            return
        return self.minData[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
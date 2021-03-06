class MyQueue(object):
    """
    用两个栈来模拟
    其中一个栈用来处理push操作，另一个栈来处理pop操作
    当第二个栈为空时，将第一个栈里的元素不断取出并放入第二个栈
    两个都为空时，empty返回True
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.popStack = []
        self.pushStack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.pushStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.popStack) != 0:
        # popStack中有元素
            return self.popStack.pop(-1)
        if len(self.pushStack) == 0:
        # 两个栈都没有元素了
            return
        while self.pushStack != []:
        # popStack中没有元素而pushStack中有元素时
            temp = self.pushStack.pop(-1)
            self.popStack.append(temp)
        return self.popStack.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.popStack) != 0:
        # popStack中有元素
            return self.popStack[-1]
        if len(self.pushStack) == 0:
        # 两个栈都没有元素了
            return
        while self.pushStack != []:
        # popStack中没有元素而pushStack中有元素时
            temp = self.pushStack.pop(-1)
            self.popStack.append(temp)
        return self.popStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.pushStack) == len(self.popStack) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
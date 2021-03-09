class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        """
        栈
        将s中元素不断压入栈中，压入之前检查栈顶元素，如果相同，则出栈且不压入
        """
        stack = []
        for letter in S:
            if stack != []:
            # 栈不为空
                if stack[-1] == letter:
                    stack.pop(-1)
                # 最后一个元素与新元素相同，相消
                    continue
            stack.append(letter)

        return "".join(stack)
                
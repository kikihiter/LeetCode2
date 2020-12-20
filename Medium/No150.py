class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 题目描述暗示得很明显，首先将括号去除，然后利用栈来存储运算
        # 实际调试过程中，发现题目给的输入数据十分纯净，不需要额外的规范化操作
        yunSuan = []    # 运算过程中存储数据的栈
        for i in range(len(tokens)):
            yunSuan.append(tokens[i])   # 读取并存储数据
            if tokens[i] == "+":
                yunSuan.pop(-1) # 去除运算符
                b = int(yunSuan.pop(-1))
                a = int(yunSuan.pop(-1))
                yunSuan.append(a+b)
            if tokens[i] == "-":
                yunSuan.pop(-1)
                b = int(yunSuan.pop(-1))
                a = int(yunSuan.pop(-1))
                yunSuan.append(a-b)
            if tokens[i] == "*":
                yunSuan.pop(-1)
                b = int(yunSuan.pop(-1))
                a = int(yunSuan.pop(-1))
                yunSuan.append(a*b)
            if tokens[i] == "/":
            # 除法运算，不用考虑除数为0的状况，题目中要求保留整数，在负数运算中，类似于“3/2”的情况，结果应为“-1”而不是“-2”
                yunSuan.pop(-1)
                b = int(yunSuan.pop(-1))
                a = int(yunSuan.pop(-1))
                if a/b<0 and a%b != 0 :
                    yunSuan.append(a/b+1)
                else:
                    yunSuan.append(a/b)
            # print yunSuan
        return int(yunSuan[-1])

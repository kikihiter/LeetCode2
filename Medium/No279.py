class Squares:
# 成功了，用一个实例存储了所有1到10000对应的值
    def __init__(self):
        self.squ = []   # 记录所有符合要求的平方数
        self.ans = {}   # 词典，记录计算完的答案
        n = 10000   # n最大为10000，将1到n全部计算出来
        t = 1
        while t*t <= n:
            self.squ.append(t*t)
            t += 1
        for i in range(1,10001):
            self.nS(i)
        
    def nS(self, m):
    # 计算m对应的答案
        if m in self.ans:
        # 如果m已经计算过
            return self.ans[m]
        if m in self.squ:
        # m的值正好是一个平方数
            self.ans[m] = 1
            return 1
        temp = float('inf')
        # temp用于记录最小的组合数
        for num in self.squ:
        # 因为m不是平方数，那么m最少由两部分组成，num以及（m-num）
            if num > m:
            # 从squ中挑选数字，作为第一部分，如果num已经比m大了，则不可能，跳出循环
                break
            if m - num in self.squ:
            # 第二部分正好是平方数的情况
                self.ans[m] = 2
                return 2
            if m - num in self.ans:
            # 第二部分已经计算过了，比较所有计算过的，取其中最小值
                a = self.ans[m-num] + 1
                temp = min(temp, a)
            # 由于计算m的过程由小到大，不存在没有计算过的第二部分
        self.ans[m] = temp
        return temp


class Solution(object):
    A = Squares()
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # t = 1
        # squ = []
        # ans = {}
        # while t*t <= n:
        #     if t*t == n:
        #         return 1
        #     squ.append(t*t)
        #     t += 1            
        
        # def nS(m):
        #     if m in ans:
        #         return ans[m]
        #     if m in squ:
        #         ans[m] = 1
        #         return 1
        #     temp = float('inf')
        #     for num in squ:
        #         if num > m:
        #             break
        #         if m - num in squ:
        #             ans[m] = 2
        #             return 2
        #         if m - num in ans:
        #             a = ans[m-num] + 1
        #             temp = min(temp, a)
        #     ans[m] = temp
        #     return temp
        
        # for i in range(1,n+1):
        #     nS(i)
        """
        上面的代码应该没什么问题
        在每次运算过程中，都要把前n个数都计算一遍，费事费力，尝试用一个对象将其存储起来
        """
        return self.A.ans[n]
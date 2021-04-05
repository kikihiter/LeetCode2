class Solution(object):
    def __init__(self):
        # nums[i]表示i*(i-1)/(i-2)的值
        self.nums = [i+1 for i in range(10001)]
        self.nums[0], self.nums[1], self.nums[2], self.nums[3], self.nums[4] = 0, 1, 2, 6, 6
        self.ans = self.nums[:]
        """
        ans[i] = ans[i-4]-2*nums[i-4] + i-3 + nums[i]
        """
        self.ans[4] = 7
        for i in range(5, 10001):
            self.ans[i] = self.ans[i-4]-2*self.nums[i-4] + i-3 + self.nums[i]
        # print self.ans


    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        210401
        3*2/1 = 6 4*3/2 = 6 5*4/3 = 6 6*5/4=7  7*6/5= 8 (n+1)*n/(n-1)
        求这个不等式成立时，n的范围，(n+2) < (n+1)*n/(n-1) < (n+3)
        n**2+2n-n-2 < n**2+n < n**2+3n-n-3
        -2 < 0 < n-3
        也就是说当n>3时(n+1)*n/(n-1)这个数比(n+2)大，但是比(n+3)小，地板除法保留整数部分也就是取(n+2)
        """
        return self.ans[N]
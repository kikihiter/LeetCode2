class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # method 1
        # i = 0
        # m = 0
        # while i != 32:
        #     if n&1 == 1:
        #         m += 1
        #     n = n >> 1
        #     i += 1
        # return m

        # method 2
        # bis = 1
        # m = 0
        # for i in range(32):
        #     if n & bis != 0:
        #         m += 1
        #     bis = bis<<1
        # return m


        # method 3
        m = 0
        while n != 0:
            n = n&(n-1)
            m += 1
        return m

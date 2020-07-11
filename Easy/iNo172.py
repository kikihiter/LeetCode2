class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        0 1
        1 1
        2 2*1 = 2
        3 3*2*1 = 6
        4 4*3*2*1 = 24
        5 5*4*3*2*1 = 120
        6 6*5*4*3*2*1 = 720
        7 5040
        8 40320
        9 362880
        10 3628800
        100 0_24 20
        99 0_22 19
        49 0_10 9
        24 4 4
        25 5 6
        """
        m = 0
        while n != 0:
            m = n/5 + m
            n = n/5
        return m
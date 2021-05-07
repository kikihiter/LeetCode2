class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        """
        210507
        0110
        1000
        1010
        """
        ans = 0
        for i in range(n):
            ans ^= 2*i + start
        return ans
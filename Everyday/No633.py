class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        """
        看起来，0也算
        """
        a, b = 0, int(c**0.5)
        d = a*a + b*b
        while d != c:
            if a == b:
                return False
            if d > c:
                b -= 1
            elif d < c:
                a += 1
            d = a*a + b*b
        return True
        
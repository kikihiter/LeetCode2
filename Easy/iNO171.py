class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        for letter in s:
            n = ord(letter)-64
            m = m*26 + n
        return m
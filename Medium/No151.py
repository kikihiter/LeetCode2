class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s.split()
        s = s[::-1]
        s = " ".join(s)
        return s 
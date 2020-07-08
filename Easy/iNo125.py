class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sList = []
        for i in s:
            if ord(i) in range(65,91):
                sList.append(i.lower())
            if ord(i) in range(97,123):
                sList.append(i)
            if ord(i) in range(48,58):
                sList.append(i)
        print sList
        k = len(sList)
        j = 0
        while j < k//2:
            if sList[j] != sList[-j-1]:
                return False
            j += 1
        return True
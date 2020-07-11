class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        7000
        269*26 + 6
        (10*26 + 9)*26 +6
        JIF
        A-Z:65-90
        0-9:48-57
        """
        def numToLe(n):
            """
            :type n:int [1,26]
            """
            return chr(n + 64)
        
        if n<1:
            return None
        ans = []
        zheng = n//26
        yu = n%26
        if yu == 0:
            zheng -= 1
            yu = 26
        ans.append(numToLe(yu))
        while zheng > 26:
            temp = zheng//26
            yu = zheng%26
            zheng = temp
            if yu == 0:
                zheng -= 1
                yu = 26
            ans.append(numToLe(yu))
        if zheng>0:
            ans.append(numToLe(zheng))
        # print ans
        return "".join(ans[::-1])

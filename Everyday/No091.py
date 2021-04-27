class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        210421
        题目结尾那个32位整型，明示用位运算，但是一时没有什么想法
        笨方法
        去除前导0
        dp[i]代表字符串s中s[:i+1]解码总数
        动态规划
        dp[i] = dp[i-2] (如果s[i-1:i+1]只有一种连接在一起的编码方式，例如10,20)这种情况下需要改写dp[i-1]的值，因为其会受到s[i]的约束
                dp[i-1] (如果s[i-1]与s[i]必然独立，例如31,27)
                dp[i-2]+dp[i-1] (s[i-1:i+1]可以拆分，例如22,11)
        """
        # def onlyOne(s1, s2):
        #     """
        #     用于判断两个字符是否只有一种解码方式
        #     返回布尔值
        #     输入为两个字符
        #     """
        #     a, b = int(s1), int(s2)
        #     if a > 2 or b == 0 or a == 0:
        #         return True
        #     if a == 2 and b > 6:
        #         return True
        #     return False
        # 阿这，突然发现，包含前导0的时候，直接返回0
        # s = s.lstrip('0')
        
        def linkType(s1, s2):
            """
            用于判断两个字符是哪种连接方式
            输入为两个字符
            返回值-1,0,1
            """
            a, b = int(s1), int(s2)
            if b == 0:
                return -1
            if a > 2 or (a==2 and b>6) or a==0:
                return 0
            return 1
        
        if not s or len(s)<1:
            return 0
        if s[0] == '0':
            return 0
        dp = [0] * len(s)
        if len(s) == 1:
            return 1
        dp[0] = 1
        if len(s) == 2:
            if s[1] == '0' and int(s[0])>2:
                return 0
            temp = linkType(s[0],s[1])
            return 1 if temp == -1 or temp == 0 else 2
        if s[1] == '0' and int(s[0])>2:
            return 0
        temp = linkType(s[0],s[1])    
        dp[1] = 1 if temp == -1 or temp == 0 else 2
        for i in range(2, len(s)):
            if s[i] == '0':
                a = int(s[i-1])
                if a > 2 or a == 0:
                    return 0
            temp = linkType(s[i-1], s[i])
            if temp == -1:
                dp[i] = dp[i-2]
                dp[i-1] = dp[i-2]
            elif temp == 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2] + dp[i-1]
            # dp[i] = dp[i-2] if onlyOne(s[i-1],s[i]) else dp[i-2] + dp[i-1]
        # print dp
        return dp[-1]
            
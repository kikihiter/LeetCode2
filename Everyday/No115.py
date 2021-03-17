class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        """
        遍历t，记录每一个字符出现在s中的位置，枚举每一种可能
        21/03/17
        本来还以为会超时的，没想到一次通过了
        """
        def dis(m, n):
            """
            计算t的第m个字符从s的第n个位置开始所包含的所有可能
            例如
            s = "rabbbit", t = "rabbit"
            m, n = 2, 2
            指的是，m=2，t的前两个字符已经确定，即'ra'确定的情况下，s从第2个索引开始即"bbbit"中有多少符合要求的组合
            """
            if m >= len(t) or n >= len(s):
                return 0
            if (m,n) in dp:
                return dp[(m,n)]
            
            char = t[m]
            chList = tDict[char]
            ans, num = 0, 0

            # 从字符char所有可能位置中挑选符合要求的位置
            for i in chList[::-1]:
                # 比n小的位置都不可能，因为是倒序遍历，剩下的点都不可能，直接跳出循环
                if i < n:
                    break
                ans += dis(m+1, i+1)
                num += 1

            # 当前点即是要找的最后一个点，满足条件的索引数量即为可能的组合数量
            if m == len(t)-1:
                dp[(m,n)] = num
                return num
            dp[(m,n)] = ans
            return ans 
            

        dp = {} # 记录dis的值
        tDict = {}  # 记录字符位置
        for i in range(len(s)):
            char = s[i]
            if char in t:
            # 字符出现在t中
                if char in tDict:
                    tDict[char].append(i)
                else:
                    tDict[char] = [i]
        
        for char in t:
            if char not in tDict:
            # 如果t中有字符不在s中，则s中没有符合条件的子序列
                # print "t中含有额外字符"
                return 0
        
        return dis(0,0)

class Solution(object):
    def __init__(self):
        self.dp = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        """
        210416
        没啥好想法
        暴搜试试
        长度到9就超时了
        """
        # dp = {}

        # def allScramble(s):
        #     """
        #     返回字符串的所有扰乱字符串
        #     """
        #     if not s:
        #         return []
        #     if s in dp:
        #         return dp[s]
        #     if len(s) == 1:
        #         dp[s] = [s]
        #         return [s]
        #     ans = []
        #     for i in range(1, len(s)):
        #         for x in allScramble(s[:i]):
        #             # print s,i
        #             for y in allScramble(s[i:]):
        #                 if x+y not in ans:
        #                     ans.append(x+y)
        #                 if y+x not in ans:
        #                     ans.append(y+x)
        #     dp[s] = ans
        #     return ans
        # print allScramble(s1)
        # return s2 in allScramble(s1)

        """
        有一个不成熟的想法
        引入“偏离值”的概念，描述每一个字符扰乱后的位置变化
        总“偏离值”应该为0
        需要注意，有重复值时，无法确定相同字符的对应关系
        不对，事实上，只要是有相同组成元素的字符串，他们之间的偏离值都为0
        """
        # if len(s1) != len(s2):
        #     return False
        # # dp1 = {}
        # # dp2 = {}
        # # for i in range(len(s1)):
        # #     ch1, ch2 = s1[i], s2[i]
        # #     if ch1 not in dp1:
        # #         dp1[ch1] = [i]
        # #     else:
        # #         dp1[ch1].append(i)
        # #     if ch2 not in dp2:
        # #         dp2[ch2] = [i]
        # #     else:
        # #         dp2[ch1].append(i)
        
        # # if len(dp1) != len(dp2):
        # #     return False
        # # ans = 0
        # # for ch in dp1.keys():
        # #     if ch not in dp2:
        # #         return False
        # dp = {}
        # ans = 0
        # for i in range(len(s1)):
        #     ch = s1[i]
        #     for j in range(len(s2)):
        #         if s2[j] == ch:
        #             if ch not in dp:
        #                 ans += j - i
        #                 dp[ch] = [j]
        #                 # print ans
        #                 break
        #             else:
        #                 if j in dp[ch]:
        #                     continue
        #                 else:
        #                     ans += j - i
        #                     dp[ch].append(j)
        #                     # print ans
        #                     break
        # return ans == 0
        """
        看了一眼答案
        """
        if (s1,s2) in self.dp:
            return self.dp[(s1,s2)]
        if len(s1) != len(s2):
            self.dp[(s1,s2)] = False
            self.dp[(s2,s1)] = False
            return False
        if s1 == s2:
            self.dp[(s1,s2)] = True
            self.dp[(s2,s1)] = True
            return True
        for ch in s1:
            if s1.count(ch) != s2.count(ch):
                self.dp[(s1,s2)] = False
                self.dp[(s2,s1)] = False
                return False
        l = len(s1)
        for i in range(1,l):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.dp[(s1,s2)] = True
                self.dp[(s2,s1)] = True
                return True
            if self.isScramble(s1[:i], s2[l-i:]) and self.isScramble(s1[i:], s2[:l-i]):
                self.dp[(s1,s2)] = True
                self.dp[(s2,s1)] = True
                return True
        self.dp[(s1,s2)] = False
        self.dp[(s2,s1)] = False
        return False

        
        
        


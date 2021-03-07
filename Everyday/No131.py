class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) < 2:
            return [[s]]
        
        dp = {} # 记录所有以key为起点的回文串终点的索引值(回文串包含右端点)
        for i in range(len(s)):
            dp[i] = []
            for j in range(i, len(s)):
                # print s[i:j+1], s[i:j+1][::-1]
                if s[i:j+1] == s[i:j+1][::-1]:
                    dp[i].append(j)
        # print dp
        parts = {}
        # 深度优先遍历dp即可
        def DFS(i):
            if i >= len(s):
                return [[]]
            if i in parts:
                return parts[i]
            ans = []
            for j in dp[i]:
                t = [s[i:j+1]]
                # print "t=",t
                pList = DFS(j+1)
                # print pList
                for p in pList:
                    # print "hello",t,p
                    ans.append(t+p)
                # ans.extend(pList)
            parts[i] = ans
            return ans
        # DFS(0)
        # print "parts",parts
        return DFS(0)

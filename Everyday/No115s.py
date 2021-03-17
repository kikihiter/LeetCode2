class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/distinct-subsequences/solution/bu-tong-de-zi-xu-lie-by-leetcode-solutio-urw3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
动态规划
其实本质上和我的方法是一样的，只不过在计算上更具有优越性
我的dp和他的dp是一个东西，他的dp是我的dp的二维展开
我的递归本身耗时耗力，他的动态规划则计算了许多无用的取值，他实际上将m*n的矩阵都计算了一遍
各有优劣，最终结果上看，我的更费时些
"""
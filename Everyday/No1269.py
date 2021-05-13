class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        """
        当长度大于steps的一半时就没有意义了，因为想要回到0处，最远就只能到steps的一半
        设f(x)的意义为经过x步回到原位的方案数，g(x)的意义为经过x步到达右侧点的方案数，显然，当可以左移时移到左侧和右侧的方案数是一致的
        f(x) = f(x-1) + g(x-1)
        g(x) = f(x-1) + f(x-2) + ... + f(0)         # 不对，从中间点x步回到中间点的方案数不等于f(x)
        f(x) = f(x-1) + f(x-2) + ... + f(-1)
        1   2    3   4   5   6   7   8   9  
        [1  2   4   9   21  51  127  323    ]
        g(x) = f(x-1) + 
        """
        """
        看了一眼答案，直接用个二维数组动规即可
        dp[i][j]表示， 经过i步落到j点的方案数
        """
        if steps<2 or arrLen<2:
            return 1
        maxL = min(steps/2, arrLen-1)
        dp = [[0]*(maxL+1) for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(1,steps+1):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % 1000000007
            l = min(i,maxL)
            for j in range(1,l+1):
                if j == l:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 1000000007
                else:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % 1000000007
        # print dp
        return dp[-1][0] # % 1000000007


        
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = []
        if len(prices) < 2:
            return 0
        for i in range(len(prices)-1):
            ans.append(max(prices[i+1:]) - prices[i])
        return max(0, max(ans))
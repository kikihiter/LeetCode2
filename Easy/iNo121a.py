class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        if len(prices) < 2:
            return 0
        i = 0
        while i < len(prices)-1:
            out = max(prices[i+1:])
            i = prices[i+1:].index(out) + i +1
            ans = max(out - min(prices[:i+1]), ans)
            i += 1
        return ans
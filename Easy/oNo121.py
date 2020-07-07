class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        minp=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            maxp=max(maxp,prices[i]-minp)
            minp=min(minp,prices[i])
        return maxp
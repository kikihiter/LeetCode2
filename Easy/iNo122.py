class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sums = 0
        haveBuy = False
        for i in range(len(prices)-1):
            if haveBuy == False and prices[i] < prices[i+1]:
                inp = prices[i]
                haveBuy = True
            if haveBuy == True and prices[i] > prices[i+1]:
                outp = prices[i]
                sums += outp - inp
                haveBuy = False
        if haveBuy == True:
            sums += prices[-1] - inp
            haveBuy = False
        return sums

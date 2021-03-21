class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        """
        没啥好说的，分成两个组，排序二分插入呗
        210321
        这题花了我几乎所有时间，做完第一题之后一直在写这个，最后一分钟交卷。里面的各种东西太容易混淆了，另外二分插入还需要继续训练，总会出点问题。
        """
        buy, sell = [], []
        def findSell(price, amount):
            # 从buy中找到合适的订单相互匹配，返回未抵消的订单数量
            # 二分查找吧，数据量很大，尽量节省时间
            if len(buy) < 1:
                return amount
            # left, middle, right = 0, 0, len(buy)-1
            # # 收购价中的最高价都小于我销售的要价，没有合适的
            # if buy[right][0] < price:
            #     return amount
            # # 找到符合我要价的最低价。。。？？？我应该找最高价啊！淦
            # while left < right:
            #     middle = (left + right)>>1
            #     if buy[middle][0] < price:
            #         left = middle + 1
            #     else:
            #         right = middle
            # 从后向前遍历buy，如果最大出价的订单未能达到我的要价，积压中不存在符合我要求的了
            while buy !=[] and buy[-1][0] >= price:
                buyPrice, buyAmount = buy.pop(-1)
                # buy中要的数量比我给的要多 
                if buyAmount > amount:
                    buy.append([buyPrice, buyAmount-amount])
                    return 0
                elif buyAmount == amount:
                    return 0
                else:
                    amount -= buyAmount
            return amount
        
        
        def findBuy(price, amount):
            # 从sell中找符合我收购条件的订单，从开头搜
            if len(sell) < 1:
                return amount
            while sell != [] and sell[0][0] <= price:
                # 频繁弹出和插入头节点，可能会比较费时
                sellPrice, sellAmount = sell.pop(0)
                if sellAmount > amount:
                    sell.insert(0, [sellPrice, sellAmount-amount])
                    return 0
                elif sellAmount == amount:
                    return 0
                elif sellAmount < amount:
                    amount -= sellAmount
            return amount
        
        def inSell(price, amount):
            # 向sell积压订单中添加新订单
            left, middle, right = 0, 0, len(sell)-1
            while left < right :
                middle = (left+right)>>1
                if sell[middle][0] < price:
                    left = middle + 1
                elif sell[middle][0] == price:
                    sell[middle][1] += amount
                    return
                else:
                    right = middle
            if left == len(sell)-1:
                if sell[left][0] < price:
                    sell.append([price, amount])
                elif sell[left][0] == price:
                    sell[left][1] += amount
                else:
                    sell.insert(left, [price, amount])
                return
            sell.insert(left, [price, amount])

        def inBuy(price, amount):
            # 向buy积压订单中添加新订单
            left, middle, right = 0, 0, len(buy)-1
            while left < right :
                middle = (left+right)>>1
                if buy[middle][0] < price:
                    left = middle + 1
                elif buy[middle][0] == price:
                    buy[middle][1] += amount
                    return
                else:
                    right = middle
            if left == len(buy)-1:
                if buy[left][0] < price:
                    buy.append([price, amount])
                elif buy[left][0] == price:
                    buy[left][1] += amount
                else:
                    buy.insert(left, [price, amount])
                return
            buy.insert(left, [price, amount])
            
        for price, amount, orderType in orders:
            if orderType == 0:
                amount = findBuy(price, amount)
                
                if amount == 0:
                    # print buy,sell
                    continue
                else:
                    inBuy(price,amount)
                    # print buy,sell
            elif orderType == 1:
                amount = findSell(price, amount)
                if amount == 0:
                    # print buy,sell
                    continue
                else:
                    inSell(price,amount)
                    # print buy,sell
        n = 0
        # print buy, sell
        while buy!= []:
            _, amount = buy.pop(-1)
            n += amount
        while sell!= []:
            _, amount = sell.pop(-1)
            n += amount
            
        return n%(10**9+7)
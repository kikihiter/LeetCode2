class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        """
        滑动窗口X
        遍历一遍数组，记录原本满意顾客数量，同时记录窗口内因为发动技能而增加的满意顾客
        """
        left = right = 0
        org = maxCha = cha = 0
        X = min(X, len(customers))
        while right < X:
        # 初始化窗口
            if grumpy[right] == 0:
            # 原本就满意
                org += customers[right]
            else:
            # 发动技能而改变的
                cha += customers[right]
            right += 1
        maxCha = max(maxCha, cha)
        while left <= right < len(customers):
        # 移动窗口
            if grumpy[right] == 0:
            # 原本就满意
                org += customers[right]
            else:
            # 发动技能而改变的
                cha += customers[right]
            if grumpy[left] == 1:
                cha -= customers[left]
            maxCha = max(maxCha, cha)
            left += 1
            right += 1 
        return maxCha + org 
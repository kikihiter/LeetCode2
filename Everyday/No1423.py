class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        """
        将问题转化为：找出数组中长度为length-k的数组，使其中数字和为最小。
        """
        if k > len(cardPoints):
        # 给定k大于数组长度，将k缩小为length
            k = len(cardPoints)
        maxS, nowS, minS = 0, 0, 0  # maxS记录数组数字总和，nowS记录当前窗口数字和，minS记录其中出现过的最小数字和
        for i in range(len(cardPoints)-k):
        # 初始化窗口
            maxS += cardPoints[i]
            # nowS += cardPoints[i]
        minS = nowS = maxS
        # print nowS
        for j in range(len(cardPoints)-k, len(cardPoints)):
            maxS += cardPoints[j]
            nowS = nowS + cardPoints[j] - cardPoints[j-len(cardPoints)+k]
            # print nowS
            minS = min(minS, nowS)
        # print minS
        return maxS - minS

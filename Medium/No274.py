class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """
        ???
        不就是二分查找吗？你还有啥新花样吗？
        """
        l = len(citations)
        left, right = 0, l-1
        while 0 <= left < right < l:
        # 找到第一个满足的论文
            middle = (left + right)>>1
            # 中值
            if citations[middle] >= l - middle:
            # 满足此条件
                right = middle
            else:
                left = middle + 1
        if l == 0:
            return 0
        if l == 1:
            if citations[0] > 0:
                return 1
            else:
                return 0
        if citations[left] < l - left:
        # left点不符合的情况，意味着全部都不符合
            return 0
        return l - left
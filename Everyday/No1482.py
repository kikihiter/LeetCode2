class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        """
        210509
        我还以为官方题解还有什么更好的解法呢
        没有！
        """
        def canMake(day):
            num = 0
            nei = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > day:
                    nei = 0
                if bloomDay[i] <= day:
                    nei += 1
                    if nei == k:
                        num += 1
                        nei = 0
                if num == m:
                    return True
            return False

        if m*k > len(bloomDay) or not bloomDay:
            return -1
        days = set(bloomDay)
        days = sorted(list(days))
        left, right = 0, len(days)-1
        while left < right:
            middle = (left+right) >> 1
            if not canMake(days[middle]):
                left = middle + 1
            else:
                right = middle
        return days[left]
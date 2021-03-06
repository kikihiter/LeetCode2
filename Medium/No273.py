class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """
        逆序排列
        """
        for i, num in enumerate(sorted(citations)[::-1]):
            if num < i+1:
                return i
        return len(citations)
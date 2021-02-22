class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        滑动窗口，右指针指到最远的地方，左指针在不满足条件的时刻右移一格，最终窗口长度即为答案
        """
        left = right = n = 0
        if K >= len(A):
            return len(A)

        while left <= right < len(A):
            if A[right] == 0:
                n += 1
            if n > K:
                if A[left] == 0:
                    n -= 1
                left += 1
            right += 1
        return right - left
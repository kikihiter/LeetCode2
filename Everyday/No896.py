class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 2:
            return True
        flag = 0
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if flag == -1:
                    return False
                else:
                    flag = 1
            if A[i] < A[i-1]:
                if flag == 1:
                    return False
                else:
                    flag = -1
        return True
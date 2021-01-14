class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        """
        从左向右读取，N_i+1 = 2*N_i + A[i]，是否能被5整除，只需要考虑个位数是0还是5
        """
        temp = 0
        answer = []
        for i in range(len(A)):
            temp = temp*2 + A[i]    # 计算当前值的个位
            temp = temp % 10    # 保留个位
            answer.append(True) if (temp == 0 or temp == 5) else answer.append(False)   # 当为0或者5时，在answer中添加True
        return answer
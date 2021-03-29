class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        # 会超时
        """
        # if len(A) < 1:
        #     return 0

        # i, n = 0, 0
        # while i < len(A)-K+1:
        #     if A[i] == 0:
        #         n += 1
        #         for j in range(K):
        #             A[i+j] = A[i+j]^1
        #     i += 1
        
        # for t in range(i,len(A)):
        #     if A[t] == 0:
        #         return -1
        # return n

        """
        210329
        补卡
        利用python数字可以无限大的一个性质
        将数组转化为二进制数字
        利用位运算来节省翻转的时间
        这个方法python里可以用
        其他语言，我就不知道了，应该要考虑用拼接的方式表示非常大的数字
        """
        # 将数组转化为数字num
        for i in range(len(A)):
            A[i] = str(A[i])
        num = "".join(A)
        num = int(num,2)
        
        changNum = 1    # 用于翻转
        flagNum = 1     # 用于判断当前位置数字是1还是0
        # 添加1到changNum里，使其形如11111
        for i in range(K-1):
            changNum <<= 1
            flagNum <<= 1
            changNum += 1
        # 左移，使位数对其，右侧不足的地方补零
        for i in range(len(A)-K):
            changNum <<= 1
            flagNum <<= 1
        n = 0   # 计数，记录翻转次数
        # 从最左位开始观察位置上的信息，如果是0的话，就将其以及后边K-1位数字取反
        for i in range(len(A)-K+1):
            if num & flagNum == 0:
                num ^= changNum
                n += 1
            changNum >>= 1
            flagNum >>= 1
        # 观察剩余部位是否还有0，有的话即不可能完成翻转
        for i in range(len(A)-K+1, len(A)):
            if num & flagNum == 0:
                return -1
            flagNum >>= 1

        return n
        
        

        

        
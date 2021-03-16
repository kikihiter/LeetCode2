class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        """
        设计一个函数，一圈一圈地填数字
        21/03/16
        """
        matrix = [[0]*n for _ in range(n)]
        
        def putNum(i, j, num, l):
            """
            :type i,j: int 要填入的第一个点的坐标
            :type num: int 要填入的第一个数字
            :type l: int 需要填入的长度
            """
            if l < 1:
                return num
            if l == 1:
                matrix[i][j] = num
                return num + 1
            # 第一行
            for k in range(l):
                matrix[i][j+k] = num
                num += 1
            
            # 右竖列
            for k in range(1, l-1):
                matrix[i+k][j+l-1] = num
                num += 1
            
            # 最后一行
            for k in range(l-1,-1,-1):
                matrix[i+l-1][j+k] = num
                num += 1
            
            # 左竖列
            for k in range(l-1-1,0,-1):
                matrix[i+k][j] = num
                num += 1
            return num
        
        mI, mNum = 0, 1
        while n > 0:
            mNum = putNum(mI,mI,mNum,n)
            mI += 1
            n -= 2
        return matrix

"""
三年前有提交记录，当时的我时间上只打败了27%
现在这个战胜了双90%
以前是直接构造矩阵，通过append等操作，现在是直接初始化一个矩阵，然后填数字
"""
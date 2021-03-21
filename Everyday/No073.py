class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        分成两个步骤
        1.遍历矩阵，遇到0，调用函数将0对应行列数值设为'X'，设'X'过程中遇到0，不设
        2.将所有'X'替换为0
        210321
        """
        def toX(i,j):
            if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
                return
            for mi in range(len(matrix)):
                if matrix[mi][j] != 0:
                    matrix[mi][j] = 'X'
            for mj in range(len(matrix[0])):
                if matrix[i][mj] != 0:
                    matrix[i][mj] = 'X'
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    toX(i,j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0
class NumMatrix(object):
    """
    记录前缀和数组
    """
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sumMat = []
        for row in matrix:
            temp = []
            s = 0
            for num in row:
                s += num
                temp.append(s)
            self.sumMat.append(temp)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = 0
        for i in range(row1, row2+1):
            s += self.sumMat[i][col2] if col1 == 0 else self.sumMat[i][col2] - self.sumMat[i][col1-1]
        return s
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
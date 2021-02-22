class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix)<2:
            return True
        if len(matrix[0])<2:
            return True

        for i in range(len(matrix)):
            a = matrix[i][0]
            t = 0
            while t+i < len(matrix) and t<len(matrix[0]):
                if matrix[i+t][t] != a:
                    return False
                t += 1
        
        for j in range(0,len(matrix[0])):
            b = matrix[0][j]
            t = 0
            while t < len(matrix) and t+j < len(matrix[0]):
                if matrix[t][j+t] != b:
                    return False
                t += 1
        return True




class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        最朴素的解法，但是在时间上实际打败了85%的人
        """
        if not matrix or len(matrix)<1 or len(matrix[0])<1:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            for j in range(len(matrix[0])):
                # print i,j
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break
        return False

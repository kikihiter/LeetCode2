class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return matrix
        ans = []
        for i in range(len(matrix[0])):
            ans.append([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j].append(matrix[i][j])
        return ans
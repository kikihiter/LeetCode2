class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        """
        21/03/15
        """
        ans = []
        while matrix != []:
            temp = matrix.pop(0)
            ans.extend(temp)
            # 第一行
            
            if matrix == []:
                return ans
            for i in range(len(matrix)):
            # 右竖列
                if matrix[i] != []:
                    ans.append(matrix[i][-1])
                    matrix[i].pop()

            temp = matrix.pop(-1)
            ans.extend(temp[::-1])
            # 最后一行

            for i in range(len(matrix)-1,-1,-1):
            # 左竖列
                if matrix[i] != []:
                    ans.append(matrix[i][0])
                    matrix[i].pop(0)

        return ans
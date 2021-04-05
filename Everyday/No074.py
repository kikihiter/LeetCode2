class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        二分查找
        """
        while not matrix or len(matrix)<1 or not matrix[0] or len(matrix[0])<1:
            return False

        up, middle, down = 0, 0, len(matrix)-1
        if matrix[up][0] > target:
            return False
        while up < down:
            # print up,middle,down
            middle = (up+down)>>1
            if matrix[middle][0] < target:
                up = middle + 1
            elif matrix[middle][0] == target:
                return True
            else:
                down = middle
        if matrix[up][0] == target:
            return True
        if up>0 and matrix[up][0] > target:
            up -= 1
        

        print up,middle,down
        left, middle2, right = 0, 0, len(matrix[0])-1
        while left < right:
            middle2 = (left+right)>>1
            if matrix[up][middle2] < target:
                left = middle2 + 1
            elif matrix[up][middle2] == target:
                return True
            else:
                right = middle2
        print left,right
        if matrix[up][left] == target:
            return True
        return False
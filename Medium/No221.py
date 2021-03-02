class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        """
        用一个长宽为l的正方形mask遮罩层，从矩阵左上角开始遍历矩阵，找到以当前点为左上角的最大正方形，记录其l
        保持l不变，移动遮罩层，如果遮罩层内不全为1，则继续遍历矩阵，若全是1，则尝试扩展mask
        """
        # if not matrix or len(matrix) < 1:
        # # 如果不存在
        #     return 0
        # l = 0
        # up = 0
        # """
        # right和down均表示mask的边界外围，mask不包含此边
        # 例如：left = up = 0, right = down =1, 表示的mask为点matrix[up][left], 此时l = 1
        # """
        # down = up + l
        # maskS = 0   # mask中数字和
        # while up <= down <= len(matrix):
        #     left = 0
        #     right = left + l
        #     while left <= right <= len(matrix[0]):
        #         while maskS == l*l
        #         # 当数字和等于面积和之时，意味着全为1，这个时候尝试扩张mask，l+=1
        #             l += 1
        #             down += 1
        #             right += 1
        #             if down == len(matrix)+1 or right == len(matrix[0])+1:
        #             # 触底了或者右边到顶了
        #                 return l-1
        #             for i in range(up, down-1):
                    


        #         left += 1
        #     up += 1

        # return l
        """
        不想写上面的方法了，细节的地方太多了，太麻烦了，换个解决方法
        计算并保存一个二维数组的前缀和矩阵，方便计算出给定区域的面积
        当面积maskS == l*l的时候，证明里面全是1
        """
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        # 矩阵不存在时
            return 0
        sList = []
        for i in range(len(matrix)):
            temp = []
            allS = 0
            for j in range(len(matrix[0])):
                t = 0
                allS += int(matrix[i][j]) 
                if i!=0:
                    t = int(sList[i-1][j])
                temp.append(allS+t)
            sList.append(temp)
        # 生成了二维前缀和矩阵

        def matS(i, j, l):
            """
            该函数的作用是返回以(i,j)为起始点，l为长度的mask面积
            """
            if l == 0:
                return 0
            if i == 0 and j == 0:
                return sList[l-1][l-1]
            elif i == 0 and j != 0:
                return sList[l-1][j+l-1] - sList[l-1][j-1]
            elif i!=0 and j==0:
                return sList[i+l-1][l-1] - sList[i-1][l-1]
            # print sList[i+l-1][j+l-1],sList[i+l-1][j-1] ,sList[i-1][j+l-1], sList[i-1][j-1]
            return sList[i+l-1][j+l-1] - sList[i+l-1][j-1] - sList[i-1][j+l-1] + sList[i-1][j-1]
        # print sList

        l = 0
        for i in range(len(matrix)):
            if i+l-1 >= len(matrix):
            # 边界条件
                break
            for j in range(len(matrix[0])):
                if j+l-1 >= len(matrix[0]) or i+l-1 >= len(matrix):
                    break
                print "help",i,j,l
                while matS(i,j,l) == l*l:
                    if i+l == len(matrix) or j+l == len(matrix[0]):
                    # l无法再变长了
                        # print "hi", i,j,l
                        l += 1
                        break
                    # print i,j,l
                    l += 1
        # print "hello"
        return (l-1)*(l-1) if l>0 else 0
            
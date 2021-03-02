class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        """
        设计一个函数来计算以(x1,y1)为左下角(x2,y2)为右上角的矩形面积，本题的重点变为找到相交矩形的左下角和右上角
        """
        def squS(x1,y1,x2,y2):
        # 返回矩形面积
            h = y2 - y1
            w = x2 - x1
            return h*w
        
        def cross(x1,y1,x2,y2,m1,n1,m2,n2):
        # 判断矩形是否相交
            if x1<x2<=m1<m2 or m1<m2<=x1<x2:
                return False
            if y1<y2<=n1<n2 or n1<n2<=y1<y2:
                return False
            return True
        
        if cross(A, B, C, D, E, F, G, H) == False:
            # print "hello"
            return squS(A,B,C,D) + squS(E, F, G, H)
        X = [A,C,E,G]
        Y = [B,D,F,H]
        X = sorted(X)
        Y = sorted(Y)
        return squS(A,B,C,D) + squS(E, F, G, H) - squS(X[1],Y[1],X[2],Y[2])
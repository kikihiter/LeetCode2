class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        """
        将原始数据转化为一个只含有0、1的二维矩阵
        例如[[5,4],[6,4],[6,7],[2,3]]，按照w由小到大以及h由小到大排列
        [2,3]
             [5,4]
             [6,4][6,7]
        转化为二维矩阵
        100
        010
        011
        
        0101010101
        1010101010
        1010010101
        1010100101
        1010100101
        1010101001
        每次套信封选择离当前点最近的（1.w上最近2.h上最近3.对角线上最近），选择其中能套最多的，递归
        
        """
        # wDict = {}
        # hDict = {}
        # for w, h in envelopes:
        #     if w in wDict:
        #         wDict[w].append(h)
        #     else:
        #         wDict[w] = [h]
        #     if h in hDict:
        #         hDict[h].append(w)
        #     else:
        #         hDict[h] = [w]
        # wList = sorted(wDict.keys())
        # hList = sorted(hDict.keys())
        # mp = []
        # for _w in wList:
        #     temp = [0 for _h in hList]
        #     mp.append(temp)
        # for w,h in envelopes:
        #     w_i = wList.index(w)
        #     h_j = hList.index(h)
        #     mp[w_i][h_j] = 1
        # # print mp
        
        # otEn = {}   # 用来存储计算过的outsideEnve(w,h)

        # def pointClose(i, j):
        # # 用来返回mp右下方区域处所有的点
        #     # # if w == 0 and h == 0:
        #     # # 初始情况
        #     # maxL = min(len(wList)-i, len(hList)-j)
        #     # for l in range(1, maxL):
        #     #     if mp[i+l][j+l] == 1:
        #     #         return [(i+l,j+l)]
        #     #     if l > 1:
        #     #         if mp[i+l][j] == 1 and[i][j+l] == 0:
        #     #             return [(i+l,j)]
        #     #         if mp[i+l][j] == 0 and[i][j+l] == 1:
        #     #             return [(i,j+l)]
        #     #         if mp[i+l][j] == 1 and[i][j+l] == 1:
        #     #             return [(i+l,j)(i,j+l)]
        #     #     return None
        #     #     # 右下方区域没有点了
        # # 最近的点不一定最好，懒得想了，所有点都返回去
        #     point = []
        #     for a in range(i+1, len(mp)):
        #         for b in range(j+1, len(mp[0])):
        #             if mp[a][b] == 1:
        #                 point.append((a,b))
        #     return point

        # def outsideEnve(i, j):
        # # 这个函数的意义是，返回长宽为wh的信件外层最多能套多少层
        #     if (i,j) in otEn:
        #     # 计算过了
        #         return otEn[(i,j)]
        #     pointList = pointClose(i,j)
        #     if pointList == []:
        #         otEn[(i,j)] = 0
        #         return 0
        #     maxEnv = 0
        #     # print pointList
        #     for point in pointList:
        #         pi,pj = point
        #         maxEnv = max(maxEnv,outsideEnve(pi,pj))
        #     # print "ot",otEn
        #     otEn[(i,j)] = maxEnv + 1
        #     return maxEnv + 1
        # print "hello"
        # return outsideEnve(-1,-1)
        """
        上边的方法应该没啥大问题，最后输在了时间限制上
        看了部分答案，知道了第300题，再来做这题
        """
        if not envelopes or len(envelopes) < 1:
            return 0
        envelopes = sorted(envelopes, key=lambda x: (x[0],-x[1]))
        # print envelopes
        ans = [envelopes[0]]
        for env in envelopes:
            w, h = env
            # print ans
            if h > ans[-1][1]:
                ans.append((w,h))
                continue
            if h < ans[-1][1]:
                # 会超时，老老实实用二分插入
                # for i in range(len(ans)):
                #     if ans[i][1] >= h:
                #         ans[i] = (w, h)
                #         break
                left , right = 0, len(ans)-1
                while left <= right <= len(ans):
                    middle = (left+right)>>1
                    if ans[middle][1] > h:
                        right = middle
                    elif ans[middle][1] < h:
                        left = middle + 1
                    elif ans[middle][1] == h:
                        break
                    if left == right:
                        middle = left
                        break
                ans[middle] = (w,h)
            
        return len(ans)
        """
        其实吧，我觉得这个运行时间跟网络环境关系很大
        没有二分插入时，我连通过都不行，一直超时
        用了二分插入，直接双百了
        """

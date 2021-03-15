class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        """
        21/03/14周赛第三题
        暂时没有啥好思路
        [1,100],[7,14],[1,1]
        
        构造一个函数，用来计算每个班级添加进一个好学生带来的影响。计算所有班级的影响因子，排列。
        """
        def YX(a,b):
            """
            a,b 为通过人数和班级人数
            """
            a = float(a)
            b = float(b)
            return (a+1)/(b+1) - a/b
        
        for cla in classes:
            pN, tN = cla
            cla.append(YX(pN,tN))
            
        classes = sorted(classes, key=lambda x:(x[2]))
        # print classes
        while extraStudents != 0:
        # 添加好学生
            pN, tN, _ = classes.pop()
            yxN = YX(pN+1, tN+1)
            # 添加新的好学生之后，更新班级信息
            
            # 将更新完的信息插入回数组，因为是排好序的，所以可以二分插入，这里直接暴力插入了
            # 果然超时了，把这里改成二分插入试试
            # for i in range(len(classes)-1,-1,-1):
            #     p_, t_, yx_ = classes[i]
            #     if yxN > yx_:
            #         if i == len(classes)-1:
            #             classes.append([pN+1,tN+1,yxN])
            #             break
            #         classes.insert(i+1, [pN+1,tN+1,yxN])
            #         break
            # else:
            # # 更新后，这个班级的影响变成最小的了，插到开头
            #     classes.insert(0, [pN+1,tN+1,yxN])
            if len(classes)==0:
                classes.append([pN+1,tN+1,yxN])
                extraStudents -= 1
                continue
            if yxN > classes[-1][-1]:
                classes.append([pN+1,tN+1,yxN])
                extraStudents -= 1
                continue
            left, right, middle = 0, len(classes)-1, 0
            while left < right:
                middle = (left+right)>>1
                p_, t_, yx_ = classes[middle]
                if yx_ < yxN:
                    left = middle + 1
                else:
                    right = middle
            
            classes.insert(left, [pN+1,tN+1,yxN])
            # print classes
            extraStudents -= 1
        
        aNum = 0
        for pN, tN, _ in classes:
            pN = float(pN)
            tN = float(tN)
            aNum += pN/tN
        
        return aNum/len(classes)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        三个想法
        1.由于不存在分数，相乘的正数越多越大，0会将整个数组分割成不含0的多个片段。
        首先遍历一遍数组，相邻的正数进行合并，用0分割数组，记录每个片段中负数的个数。
        当负数个数为偶数时，整个片段直接相乘合并（不合并了，容易出问题）；为1个时，找到这个负数前后两项，比较大小；负数为奇数且不为1时，首尾两个负数之间的数相乘合并，比较两边数大小，选大的与中间数相乘。
        最后，挑出最大的数
        2.像公交车车站票价一样，穷举任意两点之间的乘积，选择最大的
        3.利用动态规划实现2
        """
        # 第一个想法的实现
        paraList = []   # 被0分割出来的片段与片段中负数个数作为元组存入其中
        para = []   # 被分割出来的片段
        n = 0   # 用于记录负数个数
        for num in nums:
            if num > 0 :
            # 当为正数时，直接填入片段中
                para.append(num)
            elif num < 0 :
            # 为负数时，统计负数个数，并填入片段中
                para.append(num)
                n += 1
            elif num == 0:
            # 为0时，分割数组，并重置片段
                paraList.append((para, n))
                para = []
                n = 0
        if para != [] :
        # 当para不为空时，以为着有片段未存入paraList中，这是因为填入条件需要“0”，在这里添加一下
            paraList.append((para, n))

        def maxP(tup):
        # 用来计算片段中最大乘积
            para, n = tup
            if para == []:
            # 片段为空时，直接返回0
                return 0
            if n % 2 == 0:
            # 存在偶数个负数时，全部相乘即为最大
                heBing = 1
                for num in para:
                    heBing *= num
                return heBing
            # 当只存在一个负数时3
            if n == 1:
                if len(para) == 1:
                # 当只有一个元素时，返回
                    return para[0]
                left, right = 0, len(para)-1
                zuo, you = 1, 1
                while left < right:
                    if para[left] < 0:
                        break    
                    zuo *= para[left]
                    left += 1
                while left < right:
                    if para[right] < 0:
                        break
                    you *= para[right]
                    right -= 1
                return max(zuo, you)
            else:
            # 有奇数个负数，且不为1个时
                left, right = 0, len(para)-1
                zuo, zhong, you = 1, 1, 1
                while left < right:
                # 计算第一个负数及其以前各数的乘积
                    zuo *= para[left]
                    if para[left] < 0:
                        left += 1
                        break
                    left += 1
                while left < right:
                # 计算最后一个负数及其后面各数的乘积
                    you *= para[right]
                    if para[right] < 0:
                        right -= 1
                        break
                    right -= 1
                while left <= right:
                # 计算中间的数
                    zhong *= para[left]
                    left += 1
                print zuo,you,zhong
                return max(zuo*zhong, zhong*you)
        
        maxNum = float('-inf')
        for paraTup in paraList:
            maxNum = max(maxNum, maxP(paraTup))
        if maxNum < 0 and 0 in nums:
        # 由于预处理过程中会将0过滤掉，这里补上
            maxNum = 0
        return maxNum

                


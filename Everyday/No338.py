class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
        [0,1,1,2,1,2,2,3,1]
        [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,1,2,2,3]
        0,
        1
        1,2,
        1,2,2,3
        1,2,2,3,2,3,3,4,
        1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,
        1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,
        有如下规律：
        若由n位二进制数组成(不含前导0)的数字中含有1的个数集合为f(n)=[x1,x2,x3,x4...]] ，则有f(n+1) = [f(n)]+[x1+1,x2+1,x3+1...]
        """
        iDict = {0:[0],1:[1]}
        # 存储对应位数的1的个数的列表

        def getList(n):
        # 返回n位二进制1的个数的列表
            if n == 0:
                return [0]
            if n == 1:
                return [1]
            if n in iDict:
                return iDict[n]
            if n-1 in iDict:
                temp = iDict[n-1]
            else:
                temp = getList(n-1)
                iDict[n-1] = temp
            t = [x+1 for x in temp]
            iDict[n] = temp + t
            return temp + t
        
        iNum = num
        n = 0
        x = 1
        while iNum != 0:
        # 计算num的位数
            iNum = iNum>> 1
            n += 1
            x = x<<1
        x = x>>1
        # x代表num最左边的那个1
        t = x^num   # 去除了最左边的1，t代表在f(n)中只有前t个，后边的部分没有
        ans = []
        for i in range(n):
            ans.extend(getList(i))
        p = getList(n)
        ans.extend(p[:t+1])
        return ans
        """
        我的方法相当于是找规律，对于第n排的规律
        答案中的三种动态规划都很有意思，相当于是直接对单个的数字进行分析，例如数字 01010010
        1.最高有效位：
        记录最高有效位数字表示的数字 high = 01000000
        则 dict[num] = dict[num-high] + 1 = dict[00010010] + 1
        2.最低有效位：
        dict[num] = dict[num>>1] if num&1 == 0 else dict[num>>1] + 1
        这里num = 01010010 的最低有效位是 num&1 = 0
        3.最低设置位：
        找到最右侧的数字1
        这里是 num&(num-1) = 01010000
        那么dict[num] = dict[num&(num-1)] + 1
        """
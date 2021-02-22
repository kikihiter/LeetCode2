class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        m和n均转化为二进制表示，m到n，后半部分数字必定会发生变化，发生变化的位置按位与后为0，所以m和n只需要前半部分，前半部分是不发生变化的，其对应位置按位与后与之前相同。
        """
        mList, nList = [], []
        while m != 0:
        # 记录m和n的二进制数字
            a = m&1
            b = n&1
            mList.append(a)
            nList.append(b)
            m = m>>1
            n = n>>1
        # print mList, nList
        while n != 0:
        # m不足的位置补0
            a = 0
            b = n&1
            mList.append(a)
            nList.append(b)
            n = n>>1
        flag = False
        # print mList, nList
        for i in range(len(mList)-1,-1,-1):
        # 比较两个数二进制表示的数字，保留相同的前半部分，后面变为0
            if flag == True:
                mList[i] = 0
            else:
                if mList[i] != nList[i]:
                    flag = True
                    mList[i] = 0
        # print mList, nList
        ans = 0
        while mList != []:
            t = mList.pop(-1)
            ans = ans*2 + t
        
        return ans
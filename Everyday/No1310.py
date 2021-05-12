class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        """
        210512
        直接算，肯定超时
        这里先排序，如果左边界相同，从上一次右边界开始计算
        """
        # ansList = {}
        # def xor(left, right):
        #     ans = 0
        #     if (left, right) in ansList:
        #         return ansList[(left, right)]
        #     n = 0
        #     while n <= right-left:
        #         ans ^= arr[left+n]
        #         n += 1
        #     ansList[(left, right)] = ans
        #     return ans    

        # iQueries = sorted(queries)
        # iLeft, iRight = iQueries[0]
        # ansList[(iLeft, iRight)] = xor(iLeft, iRight)
        # for i in range(1, len(iQueries)):
        #     pL, pR = iQueries[i-1]
        #     nL, nR = iQueries[i]
        #     if (nL, nR) in ansList:
        #         continue
        #     if pL == nL:
        #         ansList[(nL,nR)] = xor(pR+1,nR)^ansList[(pL,pR)]
        #     else:
        #         ansList[(nL,nR)] = xor(nL,nR)
        # return [ansList[iL,iR] for iL,iR in queries]
        """
        还是超时了
        重新思考了一下
        只需要一个记录[0,n]的词典
        [i,j] = [0,j]^[0,i-1]
        进一步的，如果给的arr很长，但是所求区间却很小，实际上并不需要求全部[0,n]
        找到查询列表中左边界和右边界，求[l,r]内异或和即可
        """
        # iDict = {}
        # mostL, mostR = len(arr)-1, 0
        # for left, right in queries:
        #     if left < mostL:
        #         mostL = left
        #     if right > mostR:
        #         mostR = right
        # iDict[(mostL, mostL)] = arr[mostL]
        # tp = 1
        # while mostL + tp <= mostR:
        #     iDict[(mostL, mostL+tp)] = iDict[(mostL, mostL+tp-1)] ^arr[mostL+tp]
        #     tp += 1
        # print iDict 
        # return [iDict[mostL, r-1]^iDict[mostL, l] if r != mostL else iDict[mostL,l] for r,l in queries]     # l,r名字写反了，不打紧
        """
        很烦，不超时是不超时，为嘛优化了一下反而输给了90%的人
        我试试不优化的
        """
        dp = [0] * (len(arr)+1)
        for i in range(1,len(dp)):
            dp[i] = dp[i-1]^arr[i-1]
        return [dp[r+1] if l == 0 else dp[l]^dp[r+1] for l,r in queries]
        """
        时间上还是输给了90%的人，空间上打败了90%
        """
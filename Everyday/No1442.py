from scipy.special import comb

class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        """
        210518
        a = b       =>      a^b=0
        arr[i]^arr[i+1]^...^arr[j-1]^arr[j]^arr[j+1]^...arr[k] = 0
        设dp[i]表示从头异或到arr[i]的值，
        那么arr[i]^arr[i+1]^...^arr[j-1]^arr[j]^arr[j+1]^...arr[k] = a^b = dp[k]^dp[i-1] = 0
        [2,3,1,6,7]
        [2,1,0,6,1]
        if dp[m]] == 0:
            i = 0, k = m
        if dp[m] == dp[n]:
            i = m+1, k = n
        找到i，k后，计算j，有几个j就有几个方案
        a = dp[a] ^ dp[i-1]
        b = dp[k] ^ dp[a-1]
        遍历i到k，满足a==b的就是符合条件的j
        有大量重复值时
        dp[m] = dp[n] = dp[t]
        遍历m和n之间时找到的符合条件的j也一定满足m和t作为端点的
        时间复杂度O(N)
        """
        # dp = [0] * len(arr)
        # temp = 0
        # iDict = {}  # 用来确定右侧有没有相同值
        # iDict[0] = [-1]
        # for i in range(len(arr)):
        #     temp ^= arr[i]
        #     dp[i] = temp
        #     # iDict[temp] = 1 if temp not in iDict else iDict[temp] + 1
        #     if temp in iDict:
        #         iDict[temp].append(i)
        #     else:
        #         iDict[temp] = [i]
        # # if 0 in iDict and iDict[0][0] == 0:
        # #     iDict[0],pop(0)
        # #     if iDict[0] == []:
        # #         del iDict[0]
        # # left, middle, right = 0, 0, 0
        # # flag = True
        # # ans = 0
        # # while len(iDict[0])>0:
        # #     if flag:
        # #         ans += comb(len(iDict[0]),2)
        # #         flag = False
        # #     right = iDict[0].pop(0)
        # #     n = 0
        # #     while middle <= right:
        # #         if middle > 0 and dp[middle-1] == dp[right]^dp[middle-1]:
        # #             n += 1
        # #             print left,middle,right
        # #         middle += 1
        # #     left = right
        # #     ans += (len(iDict[0])+1)*n
        # # print ans
        # ans = 0
        # flag = {}
        # for i in range(len(arr)):
        #     if len(iDict[dp[i]]) < 2:
        #         continue
        #     if dp[i] not in flag:
        #         ans += comb(len(iDict[dp[i]]),3)
        #         flag[dp[i]] = []
        #     left = iDict[dp[i]].pop(0) + 1
        #     middle = left + 1
        #     right = iDict[dp[i]][0]
        #     n = 0
        #     while middle <= right:
        #         if left == 0:
        #             a = dp[middle]
        #         else:
        #             a = dp[middle] ^ dp[left-1]
        #         if a == dp[right] ^ dp[middle]:
        #             n += 1
        #             # print left,middle,right
        #         middle += 1
        #     flag[dp[i]].append(n)
        #     # ans += (len(iDict[dp[i]]))*n
        # for iKey in flag.keys():
        #     ans += sum(flag[iKey]) * len(flag[iKey])
        # return int(ans)
        """
         0 1 2 3 4 
        [1,1,1,1,1]
        [1,0,1,0,1]
        011 013 024 023 122 124 134 144 233 344 033
        011 013 024 023 122 124         233 344
        """
        """
        想错了，原来确定了i、k之后，其中任意j都能符合条件
        """
        dp = [0] * len(arr)
        iDict = {}
        iDict[0] = [-1]
        temp = 0
        for i in range(len(arr)):
            temp ^= arr[i]
            dp[i] = temp
            if temp in iDict:
                iDict[temp].append(i)
            else:
                iDict[temp] = [i]
        ans = 0
        for iKey in iDict.keys():
            iList = iDict[iKey]
            l = len(iList)
            if l < 2:
                continue
            # 以iList[i]为左端点
            for i in range(l-1):
                # 以iList[k]为右端点
                for k in range(i+1, l):
                    ans += iList[k] - iList[i] - 1
        return ans

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        应当注意，不同的数可能拥有相同的频次，用numList记录所有这些数(会超时)
        """
        # n = 0
        # numList = []
        # allList = []
        # for num in nums:
        #     t = nums.count(num)
        #     if num in allList:
        #         continue
        #     allList.append(num)
        #     print allList
        #     if t == n:
        #         if num in numList:
        #             continue
        #         else:
        #             numList.append(num)
        #     if t > n:
        #         n = t
        #         numList = [num]
        # ans = float('inf')
        # print numList
        # while numList != []:
        #     print numList
        #     a = numList.pop()
        #     l = len(nums) - nums.index(a) - nums[::-1].index(a)
        #     ans = min(l, ans)
        # return ans
        """
        用答案的方式来做
        """
        numDict = {}
        for i, num in enumerate(nums):
            if num in numDict:
                numDict[num][0] += 1
                numDict[num][-1] = i
            else:
                numDict[num] = [1, i, i]
        
        maxN = 0 
        l = float('inf')
        # print numDict
        for a in numDict.values():
            if a[0] > maxN:
                l = a[-1] - a[1]
                maxN = a[0]
            elif a[0] == maxN:
                t = a[-1] - a[1]
                l = min(t,l)

        return l+1

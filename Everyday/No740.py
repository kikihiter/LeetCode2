class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        210505
        词典计数,并排序
        有点像小偷偷东西不触发警报那题
        """
        numDict = {}
        for num in nums:
            numDict[num] = 1 if num not in numDict else numDict[num] + 1
        dp = [0] * len(numDict)
        keyList = sorted(numDict.keys())
        dp[0] = numDict[keyList[0]]*keyList[0]
        if len(keyList) > 1:
            dp[1] = numDict[keyList[1]]*keyList[1] if keyList[1] == keyList[0]+1 else dp[0] + numDict[keyList[1]]*keyList[1]
        else:
            return dp[0]
        if len(keyList) > 2:
            if keyList[2] > keyList[1]+1:
                dp[2] = max(dp[0], dp[1]) + numDict[keyList[2]]*keyList[2]
            else:
                dp[2] = dp[0] + numDict[keyList[2]]*keyList[2]
        else:
            return max(numDict[keyList[0]]*keyList[0], numDict[keyList[1]]*keyList[1]) if keyList[1]==keyList[0]+1 else numDict[keyList[0]]*keyList[0] + numDict[keyList[1]]*keyList[1]
        
        for i in range(3,len(keyList)):
            if keyList[i] == keyList[i-1]+1:
                dp[i] = max(dp[i-3],dp[i-2]) + numDict[keyList[i]]*keyList[i]
            else:
                dp[i] = max(dp[i-2],dp[i-1]) + numDict[keyList[i]]*keyList[i]
        # print numDict,keyList
        # print dp
        return max(dp[-1],dp[-2])


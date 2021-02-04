class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        计算窗口中的平均数，不断移动窗口，将上一个数字移除，下一个填入。
        """
        if k>len(nums):
            k = len(nums)
        sumN = 0
        for i in range(k):
        # 计算初始窗口内数字总合
            sumN += nums[i]
        ave = float(sumN)/k
        
        for i in range(len(nums)-k):
            sumN = sumN - nums[i] + nums[i+k]
            t = float(sumN)/k
            ave = max(ave, t)
        return ave
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        210325
        动态规划，dp[i]表示以nums[i]结尾的子数组的最大和
        """
        if not nums:
            return 
        maxSum = nums[0]  # 记录最大和
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
            maxSum = max(maxSum, dp[i])
        return maxSum
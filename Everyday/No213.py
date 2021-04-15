class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        动态规划
        210415
        两个月前做过
        两个dp，一个记录不偷第一家的，一个记录偷第一家的
        """
        if len(nums) < 4:
            return max(nums)
        dp1 = [0]*len(nums)
        dp2 = [0]*len(nums)
        dp1[0], dp1[1], dp1[2] = nums[0], nums[1], nums[0]+nums[2]
        dp2[1], dp2[2] = nums[1], nums[2]
        for i in range(3, len(nums)):
            dp1[i] = max(dp1[i-2],dp1[i-3]) + nums[i]
            dp2[i] = max(dp2[i-2],dp2[i-3]) + nums[i]
        return max(dp1[-2], dp2[-1], dp1[-3])

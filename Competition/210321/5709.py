class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        210321
        """
        if not nums or len(nums) < 1:
            return
        if len(nums) == 1:
            return nums[0]
        maxSum, nowSum = nums[0], nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                nowSum += nums[i]
                maxSum = max(maxSum, nowSum)
            elif nums[i] <= nums[i-1]:
                maxSum = max(maxSum, nowSum)
                nowSum = nums[i]
        return maxSum
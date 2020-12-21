class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        # 看了答案后，自己写写试试
        minF = maxF = ans = nums[0]
        for i in range(1, len(nums)):
            mx, mn = maxF, minF
            maxF = max(mx*nums[i], mn*nums[i], nums[i])
            minF = min(mx*nums[i], mn*nums[i], nums[i])
            ans = max(ans, maxF)
        return ans
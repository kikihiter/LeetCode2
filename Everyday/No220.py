class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        """
        之前做过
        210417
        上次是滑动窗口内部排序的方法做的
        这次用桶
        """
        k = min(len(nums)-1, k)
        i = 0
        dp = {}
        while i <= k:
            a = nums[i]/(t+1)
            if a in dp:
                return True
            else:
                dp[a] = nums[i]
            if a-1 in dp and abs(dp[a]-dp[a-1])<=t:
                return True
            if a+1 in dp and abs(dp[a]-dp[a+1])<=t:
                return True
            i += 1
        while i < len(nums):
            a = nums[i-k-1]/(t+1)
            del dp[a]
            b = nums[i]/(t+1)
            if b in dp:
                return True
            else:
                dp[b] = nums[i]
            if b-1 in dp and abs(dp[b]-dp[b-1])<=t:
                return True
            if b+1 in dp and abs(dp[b]-dp[b+1])<=t:
                return True
            i += 1
        return False


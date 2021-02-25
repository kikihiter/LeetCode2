class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            dp1, dp2 = 0, 0
            for num in nums:
                dp2, dp1 = max(dp1 + num, dp2), dp2
            return dp2
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

作者：Nicosauto
链接：https://leetcode-cn.com/problems/house-robber-ii/solution/python-by-nicosauto-s52d/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
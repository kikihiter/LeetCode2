class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:
                return True
            while candidate_k and nums[i] > candidate_k[-1]:
                max_k = candidate_k[-1]
                candidate_k.pop()
            if nums[i] > max_k:
                candidate_k.append(nums[i])

        return False

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-solution-ye89/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
对数字1(nums[i])进行枚举
"""
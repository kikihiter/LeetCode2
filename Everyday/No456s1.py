class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # 左侧最小值
        left_min = nums[0]
        # 右侧所有元素
        right_all = SortedList(nums[2:])
        
        for j in range(1, n - 1):
            if left_min < nums[j]:
                index = right_all.bisect_right(left_min)
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_all.remove(nums[j + 1])

        return False

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-solution-ye89/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
对数字3(nums[k])进行枚举
"""
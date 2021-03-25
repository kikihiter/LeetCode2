class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        candidate_i, candidate_j = [-nums[0]], [-nums[0]]

        for v in nums[1:]:
            idx_i = bisect.bisect_right(candidate_i, -v)
            idx_j = bisect.bisect_left(candidate_j, -v)
            if idx_i < idx_j:
                return True

            if v < -candidate_i[-1]:
                candidate_i.append(-v)
                candidate_j.append(-v)
            elif v > -candidate_j[-1]:
                last_i = -candidate_i[-1]
                while candidate_j and v > -candidate_j[-1]:
                    candidate_i.pop()
                    candidate_j.pop()
                candidate_i.append(-last_i)
                candidate_j.append(-v)

        return False

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-solution-ye89/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
枚举数字2(nums[j])
很遗憾的是，这三个解法都和我有本质上的不同
"""
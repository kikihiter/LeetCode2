class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        accDiff = [0] + list(accumulate(abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)))
        maxLength = 0

        for i in range(1, n + 1):
            start = bisect.bisect_left(accDiff, accDiff[i] - maxCost)
            maxLength = max(maxLength, i - start)
        
        return maxLength

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/get-equal-substrings-within-budget/solution/jin-ke-neng-shi-zi-fu-chuan-xiang-deng-b-higz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
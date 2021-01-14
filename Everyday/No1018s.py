class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = list()
        prefix = 0
        for num in A:
            prefix = ((prefix << 1) + num) % 5
            ans.append(prefix == 0)
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/solution/ke-bei-5-zheng-chu-de-er-jin-zhi-qian-zh-asih/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
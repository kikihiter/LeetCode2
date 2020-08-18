class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1

作者：LeetCode
链接：https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
官方给出的答案非常之精妙，特别是证明那一段。可惜正如评论区说的，官方的解释总是差强人意。实际上，官方这解法可以转化为方法二。每次更新的时候，实际上就是在求方法二中的最小点。
"""
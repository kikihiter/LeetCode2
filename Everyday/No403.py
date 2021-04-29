class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        """
        210429
        递归，记忆化存储
        """
        memo = {}
        l = len(stones)
        # 为了通过类似测试用例[0,2]
        if stones[1] - stones[0] != 1:
            return False

        def xkCan(x, k):
            """
            假设在第x号石头上，上一步跳了k步
            返回布尔值，表示是否可以跳到最后
            """
            # 记忆化存储，已经计算过这个节点了
            if (x, k) in memo:
                return memo[(x,k)]
            # 已经在最后一颗石头上了
            if x == l - 1:
                memo[(x,k)] = True
                return True
            # 记录跳k步落到的石头数值
            nextSt = stones[x] + k
            for i in range(1, len(stones[x:])):
                # 最远k+1步都到达不了x+i号石头，已经不可能成功了
                if stones[x+i] > nextSt + 1:
                    memo[(x,k)] = False
                    return False
                # 跳k-1步可以落到x+i号石头
                if stones[x+i] == nextSt -1:
                    if xkCan(x+i, k-1):
                        memo[(x,k)] = True
                        return True
                # 跳k步
                if stones[x+i] == nextSt:
                    if xkCan(x+i, k):
                        memo[(x,k)] = True
                        return True
                # 跳k+1步
                if stones[x+i] == nextSt + 1:
                    if xkCan(x+i, k+1):
                        memo[(x,k)] = True
                        return True
            # 在剩余石头中，找不到可以跳到最后的方案
            memo[(x,k)] = False
            return False

        return xkCan(1,1)

            
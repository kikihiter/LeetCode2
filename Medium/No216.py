
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        def rightSum(left, rN, rSum):
        # 计算数字left右侧有几种情况可以使rN个数相加等于rSum
            if left > 9 or rSum < 0:
                return
            if rN == 1:
            # 只有一个数字时
                for num in range(left, 10):
                    if num == rSum:
                    # 有num等于所求和时
                        return [[num]]
                else:
                    return
            ans = []
            for i in range(left, 11-rN):
                temp = rightSum(i+1, rN-1, rSum-i)
                if temp and len(temp) > 0:
                    for t in temp:    
                        t.append(i)
                    ans.extend(temp)
            return ans

        return rightSum(1, k, n)
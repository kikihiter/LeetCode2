class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == []:
            return 0
        sums = [triangle[0][0]]
        n = len(triangle)
        if n == 1:
            return sums[0]
        while n != 1:
            temp = []
            temp.append(sums[0] + triangle[-n+1][0])
            for m in range(1, len(triangle[-n+1])-1):
                he = min(sums[m-1], sums[m]) + triangle[-n+1][m]
                temp.append(he)
            temp.append(sums[-1] + triangle[-n+1][-1])
            sums = temp
            n -= 1
        return min(sums)
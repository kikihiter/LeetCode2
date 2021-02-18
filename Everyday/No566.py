class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return nums

        r0 = len(nums)
        l0 = len(nums[0])
        if r0 * l0 != r*c:
            return nums
        
        ans = []
        temp = []
        for i in range(r0):
            for j in range(l0):
                temp.append(nums[i][j])
                if len(temp) == c:
                    ans.append(temp)
                    temp = []
        return ans
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        maxI, l = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                l = 0
            else:
                l += 1
                maxI = max(maxI, l)
            i += 1
        return maxI
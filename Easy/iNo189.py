class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        while k != 0:
            temp = nums[-1]
            del nums[-1]
            nums.insert(0,temp)
            k -= 1
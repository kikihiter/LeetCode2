class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        210409
        做过
        """
        left, right = 0, len(nums)-1
        while left < right:
            middle = (left+right)>>1
            if nums[left] < nums[right]:
                return nums[left]
            elif nums[left] > nums[right]:
                if nums[middle] >= nums[left]:
                    left = middle + 1
                else:
                    right = middle
            elif nums[left] == nums[right]:
                left += 1
        return nums[left]

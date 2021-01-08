class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        题目要求时间复杂度O(logN)，一般这样就是二分法或类似结构。
        二分法需要一个选择左或右的判断，这里根据中心点未来升降趋势选择。
        """
        # nums.insert(0, float('-inf'))
        # nums.append(float('-inf'))
        left, mid, right = 0, 0, len(nums)-1
        while left < right:
            if left + 1 == right:
                mid = left if (nums[left]>nums[right]) else right
                break
            mid = (left + right)/2
            if nums[mid] > nums[mid+1]:
                right = mid
                continue
            else:
                left = mid
                continue
        return mid
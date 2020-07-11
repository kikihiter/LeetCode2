class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for num in nums:
            if num in temp:
                continue
            if nums.count(num) > len(nums)/2:
                return num
            temp.append(num)
        
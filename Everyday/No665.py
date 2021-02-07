class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        遍历数组，记录下异常点，异常点数量大于1，则返回false
        针对异常点，进行分析
        """
        if len(nums) <= 2:
        # 只有一个或没有数字时，直接返回True
            return True
        err = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if err != 0:
                    return False
                else:
                    err = i
        if err > 1 and nums[err] >= nums[err-2]:
            return True
        if err < len(nums)-1 and nums[err+1] >= nums[err-1]:
            return True
        if err <= 1 or err == len(nums)-1:
            return True
        return False 
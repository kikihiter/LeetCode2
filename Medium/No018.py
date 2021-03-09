class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        排序
        2021/03/09
        """
        if not nums or len(nums) < 4:
            return []

        nums = sorted(nums)
        print nums
        ans = []
        for i in range(len(nums)-3):
            if nums[i] > target and nums[i+1] >= 0:
                break
            for j in range(i+1, len(nums)-2):
                if nums[i] + nums[j] > target and nums[j+1] >= 0:
                    break
                left, right = j+1, len(nums)-1
                while left < right:
                    s = nums[i]+nums[j]+nums[left]+nums[right]
                    # print s
                    if s == target:
                        temp = [nums[i], nums[j], nums[left], nums[right]]
                        if temp not in ans:
                            ans.append(temp)
                        left += 1
                        right -= 1
                    elif s > target:
                        right -= 1
                    elif s < target:
                        left += 1
        return ans
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        """
        划窗，移动left，每次移动的时候，找到最近可能的right，记录长度
        """
        left = right = 0
        numSum = 0
        l = float('inf')
        while left < len(nums):
            while numSum < target and right < len(nums):
                numSum += nums[right]
                right += 1
            else:
            # 循环结束时，有两种情况，第一种是numSum不小于target，第二种情况是right到头了
                if numSum < target:
                # 这意味着，是right到头而结束的循环
                    if left == 0:
                    # 如果此时left没有动过，也就是说所有数字加起来都达不到target
                        return 0
                    else:
                    # left移动过，只是当前窗口全部相加达不到target，则left不需要再继续移动了
                        break
            l = min(l, right-left)
            numSum -= nums[left]
            left += 1
            
        return l
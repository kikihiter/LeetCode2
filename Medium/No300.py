class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        方法二的解法，尝试自己写出来
        """
        if not nums or len(nums) < 1:
            return 0
        ans = [nums[0]]
        # ans[i]表示长度为i+1的子序列末尾最小值组成的集合
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
            # 比最后一个值大，直接在后面添加
                ans.append(nums[i])
                continue
            if nums[i] < ans[-1]:
                for j in range(len(ans)):
                    if ans[j] >= nums[i]:
                        ans[j] = nums[i]
                        break
        
        return len(ans)
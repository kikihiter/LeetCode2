class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        看了部分答案，用两个列表来存储信息
        一个存储当前位置左边所有数的乘积，一个存储右边的乘积
        则中间的数字为左右两个乘积
        """
        ans = []
        left = 1
        for i in range(1,len(nums)):
        # 生成列表，存储信息
            left *= nums[i-1]
            ans.append(left)
        ans.insert(0,1)
        # 在最前面补上1，使数组长度相等

        right = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
            # 右端点，不需要改变
                continue
            right *= nums[i+1]
            # 右边各数的累乘
            ans[i] *= right
        return ans
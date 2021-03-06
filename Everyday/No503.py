class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        最朴素的想法是遍历数组，找到比当前数字高的下一个数字
        但是在找到下一个数字的过程中，会浪费大量的时间
        尝试在此过程中，记录此间数字信息，对其进行插入排序
        例如
        [1,2,1,-5,6,7,8,5,2]
        l = 1   r = 1
        ans = [] cha = [10]
        l = 1   r = 2
        ans = [2] cha = [2]
        l = 2   r = 1
        ans = [2] cha = [1,2]
        l = 2   r = -5
        ans = [2] cha = [-5,1,2]
        l = 2   r = 6
        ans = [2,6] cha = [-5,1,6]
        l = 1   r = 6
        ans = [2,6,6] cha = [-5,6]
        l = -5   r = 6
        ans = [2,6,6,6] cha = [6]
        l = 6   r = 6
        ans = [2,6,6,6] cha = [6]
        l = 6   r = 7
        ans = [2,6,6,6,7] cha = [7]
        l = 7   r = 8
        ans = [2,6,6,6,7] cha = [8]
        
        
        [8,-19,5,-4,20]
        这个方法不对，上面这个例子就会出错
        """
        # if not nums or len(nums) < 1:
        #     return []
        # if len(nums) == 1:
        #     return [-1]
        # maxNum = nums[0]

        # for num in nums:
        #     maxNum = max(maxNum,num)
        # # 找到最大数
        
        # channel = []
        # ans = []
        # left = right = 0
        # flag = False
        # # 整个过程分为两个阶段，一个是移动right，往channel中添加数字的阶段，一个是移动left，往ans中添加，从channel中删除的阶段，用flag来标识
        # while 0 <= left < len(nums):
        # # right读到的数字都存入channel中，left对应的数字从channel中删除
        #     # if nums[left] == 0 and 
        #     if right >= len(nums):
        #         right -= len(nums)
        #     if flag == False:
        #     # 添加进channel的阶段
        #         if left == right and nums[left] == maxNum:
        #             ans.append(-1)
        #             left += 1
        #             right += 1
        #             flag = False
        #             continue
        #         if nums[right] > nums[left]:
        #         # right比left大,即left的下一个更大的数
        #             ans.append(nums[right])
        #             channel.remove(nums[left])
        #             channel.append(nums[right])
        #             left += 1
        #             # right += 1
        #             flag = True # 移动了left，改变阶段
        #             continue
        #         # right不是要找的数，将其二分插入至channel中
        #         l, r = 0, len(channel)-1
        #         # print channel,"hello"
        #         while 0 <= l < r < len(channel):
        #             m = (l+r)>>1
        #             if channel[m] >= nums[right]:
        #                 r = m
        #             elif channel[m] < nums[right]:
        #                 l = m + 1
        #         channel.insert(l, nums[right])
        #         # print channel
        #         right += 1
        #         continue
        #     elif flag == True:
        #     # right已经在channel中了
        #         if left != right:
        #         # channel中一定有left的下一个更大的数，二分查找
        #             l, r = 0, len(channel)-1
        #             while 0 <= l < r < len(channel):
        #                 m = (l+r)>>1
        #                 if channel[m] > nums[left]:
        #                     r = m
        #                 elif channel[m] <= nums[left]:
        #                     l = m + 1
        #             # print channel,l,r
        #             ans.append(channel[l])
        #             channel.remove(nums[left])
        #             left += 1
        #             flag = True
        #         elif left == right:
        #         # channel中只有一个元素
        #             if nums[left] == maxNum:
        #                 channel = []
        #                 ans.append(-1)
        #                 left += 1
        #             right += 1
        #             flag = False
        
        # return ans
        """
        用一个栈来记录没有找到下一个更大的数的数字
        方向想错了，特别复杂，想对了之后，一下子就做出来了
        """
        if not nums or len(nums) < 1:
            return []
        if len(nums) == 1:
            return [-1]

        ans = [-1 for _ in nums]
        stack = []
        for i, num in enumerate(nums):

            if stack == []:
            # 栈中为空，直接丢进去
                stack.append((i,num))
                continue

            while stack != [] and num > stack[-1][1]:
            # 当前数比最后一个大
                i1, num1 = stack.pop(-1)
                ans[i1] = num
            stack.append((i,num))
        
        for num in nums:
            if len(stack) == 1:
            # 栈中只剩最大的那个数字了
                break
            while stack != [] and num > stack[-1][1]:
            # 当前数比最后一个大
                i1, num1 = stack.pop(-1)
                ans[i1] = num
        return ans

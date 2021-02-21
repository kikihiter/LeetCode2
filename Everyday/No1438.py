class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        """
        滑动窗口，建立一个与窗口拥有相同元素的列表，对列表进行插入排序
        会超时
        """
        # if len(nums)<1:
        #     return 0
        # channel = []
        # left = right = 0
        # while left <= right < len(nums):
        #     for i in range(len(channel)):
        #     # 插入第right个元素
        #         if nums[right] < channel[i]:
        #             channel.insert(i, nums[right])
        #             break
        #     else:
        #     # 在末尾
        #         channel.append(nums[right])
            
        #     if channel[-1] - channel[0] > limit:
        #     # 超出限制
        #         channel.remove(nums[left])
        #         # 在channel中删除nums[left] 
        #         left += 1
        #         # 右移一格left

        #     right += 1
        # # print channel
        # return right - left
        """
        试试直接用max和min
        还是超时
        """
        # if len(nums)<1:
        #     return 0
        # left = right = 0
        # while left <= right < len(nums):
        #     maxNum = max(nums[left:right+1])
        #     minNum = min(nums[left:right+1])
        #     if maxNum - minNum > limit:
        #     # 超出限制
        #         left += 1
        #         # 右移一格left
        #     right += 1
        # return right - left
        """
        试试用哈希表记录窗口数据
        """
        if len(nums)<1:
            return 0
        numDict = {}
        left = right = 0
        maxNum = minNum = nums[0]
        while left <= right < len(nums):
            # 将right端元素加入进numDict中
            if nums[right] not in numDict:
            # 不存在，则新建并初始化为1
                numDict[nums[right]] = 1
            else:
            # 存在，则++
                numDict[nums[right]] += 1
            if nums[right] > maxNum:
            # 新加入元素比窗口最大值大，则更新最大值
                maxNum = nums[right]
            if nums[right] < minNum:
            # 更新最小值
                minNum = nums[right]
            if maxNum - minNum > limit:
            # 超出限制
                if numDict[nums[left]] > 1:
                # 窗口中还有相同的元素，不影响结果，同时右移左右两端点，并--
                    numDict[nums[left]] -= 1
                    left += 1
                    right += 1
                    continue
                if nums[left] == maxNum:
                # 需要移出窗口的左端点正好为最大值且数量为1
                    del numDict[maxNum]
                    # 删除此点
                    maxNum = max(numDict.keys())
                    # 更新最大值
                elif nums[left] == minNum:
                    del numDict[minNum]
                    minNum = min(numDict.keys())  
                else:
                # 既不是最大值也不是最小值，直接删除
                    del numDict[nums[left]]
                left += 1
                # 右移一格left
            right += 1
        return right - left

        
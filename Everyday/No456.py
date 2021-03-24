class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        210324
        从头遍历数组
        记录所有升序区间（不含端点），后续如果有数据落在区间上，则True
        """
        # 不足三个元素时，直接返回
        if not nums or len(nums) < 3:
            return False
        i = 1
        # 找到第一个谷底，作为第一个升序区间的起始点
        while i < len(nums):
            if nums[i] > nums[i-1]:
                break
            i += 1
        # 遍历完整个数组，却找不到降序，后半部分全部为升序，直接返回False
        else:
            return False
        # 将升序序列存储在shxList中
        shxList = []
        temp = [nums[i-1], nums[i]]
        while i < len(nums):
            # print i , temp, shxList
            if shxList != []:
                # 从后向前遍历升序序列，因为后面的序列可能会覆盖前面的部分，更容易弹出
                for shx in shxList[::-1]:
                    # 当前节点落在区间内
                    if nums[i] > shx[0] and nums[i] < shx[1]:
                        return True
            # 还在升序
            if nums[i] > nums[i-1]:
                temp[1] = nums[i] # 更新升序区间的尾端
            # 相等元素毫无贡献，直接跳过
            elif nums[i] == nums[i-1]:
                i += 1
                continue
            # 比前一个元素小，开始下坡
            else:
                # 如果这个元素正好落在当前升序区间内，直接返回True
                if nums[i] > temp[0]:
                    return True
                # 开始降序，找到谷底，降序部分有个特性，如果降序的第一个节点不满足要求的话，后续所有的节点都不可能满足要求
                else:
                    if temp[0] != temp[1]:
                        shxList.append(temp)
                    # 找到降序的最后一个节点
                    while i < len(nums):
                        if nums[i] > nums[i-1]:
                            break
                        i += 1
                    # 后续没有升序了，直接返回False
                    else:
                        return False
                    i -= 1
                    temp = [nums[i],nums[i+1]]  # 更新升序区间
            i += 1
        return False
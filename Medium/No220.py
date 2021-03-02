class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        """
        维持一个大小为k+1滑窗，对滑窗中的数字进行排序，遍历排序后的数组，找到差值最小的两个数，并记录下这两个端点
        移动划窗时，新加入的数按大小插入窗口，比较插入位置左右两数与插入数值的差值大小，并与记录中的差值做比较，更新差值最小的组合
        如果差值最小的组合中有端点被移出窗口，此时，重新遍历窗口，找到新的差值最小值
        """
        if k == 0 or len(nums) < 2:
            return False
        k = min(k, len(nums)-1)
        channel = nums[:k+1]    # 初始化窗口
        channel = sorted(channel)   # 排序
        cha = float('inf')
        # chaCouple = (0, 0)
        for i in range(k):
            temp = channel[i+1] - channel[i]
            # 计算差值
            if temp <= cha:
                cha = temp
                chaCouple = [channel[i], channel[i+1]]
                # 更新最小差值，并记录两端点数值
        # print cha, channel
        if cha <= t:
            # print "fuck"
            return True
        # print "hello"
        update = False
        for left in range(1, len(nums)-k):
            right = left + k
            if nums[left-1] in chaCouple:
            # 左端点的数正好是差值最小值的端点，则需要更新
                update = True
            channel.remove(nums[left-1])
            for i in range(len(channel)):
            # 插入新来的数字
                if nums[right] == channel[i]:
                    return True
                if nums[right] < channel[i]:
                    channel.insert(i, nums[right])
                    # if i == 0:
                    #     iLeft = float('inf')
                    # else:
                    #     iLeft = channel[i] - channel[i-1]
                    iLeft = float('inf') if i == 0 else channel[i] - channel[i-1]
                    # if i == len(chaCouple)-1:
                    #     iRight = float('inf')
                    # else:
                    #     iRight = channel[i+1] - channel[i]
                    iRight = float('inf') if i == len(chaCouple)-1 else channel[i+1] - channel[i]
                    if iLeft <= iRight and iLeft <= cha:
                    # 如果新插入而诞生的新的差值比最小差值小，则不需要重新遍历数组，直接更新最小值
                        update = False
                        cha = iLeft
                        chaCouple = [nums[i-1], nums[i]]
                    elif iRight < iLeft and iRight <= cha:
                        update = False
                        cha = iRight
                        chaCouple = [nums[i], nums[i+1]]
                    break
            else:
            # 插入在了最后面
                channel.append(nums[right])
                iLeft = channel[-1] - channel[-2]
                if iLeft <= cha:
                    update = False
                    cha = iLeft
                    chaCouple = [nums[-2], nums[-1]]
            if update == True:
            # 需要重新遍历窗口
                cha = float('inf')
                for i in range(len(channel)-1):
                    temp = channel[i+1] - channel[i]
                    if temp <= cha:
                        cha = temp
                        chaCouple = [channel[i], channel[i+1]]
                update = False
            if cha <= t:
                # print cha, channel
                return True
            # print left,channel
        return False
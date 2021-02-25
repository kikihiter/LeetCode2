class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        递归，用一个参数来描述是否可以取最后一个值
        """
        l = len(nums)
        iDict = {}

        def iRob(flag, iL):
            """
            flag为布尔值，当为True时，意味着不可以取最后一位
            """
            if iL >= l:
                return 0
            if iL == l-1:
                if flag == True:
                # 不可取时
                    return 0
                else:
                    return nums[-1]
            if iL == l-2:
                # 有两个数时
                if flag == True:
                    # 不可取
                    return nums[-2]
                else:
                    return max(nums[-1], nums[-2])
            if iL == l-3:
                if flag == True:
                    return max(nums[-2], nums[-3])
                else:
                    return max(nums[-3]+nums[-1], nums[-2])
            if (flag, iL) in iDict:
                return iDict[(flag, iL)]
            if (flag, iL+2) not in iDict:
                iDict[(flag, iL+2)] = iRob(flag, iL+2)
            a = nums[iL] + iDict[(flag, iL+2)]
            if (flag, iL+3) not in iDict:
                iDict[(flag, iL+3)] = iRob(flag, iL+3)
            b = nums[iL+1] + iDict[(flag, iL+3)]
            # print flag, numsList,a,b
            return max(a, b)

        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        a = nums[0] + iRob(True, 2)
        b = nums[1] + iRob(False, 3)
        c = iRob(False, 2)   # [1,2,3,4,5,1,2,3,4,5]不加的话，这个例子通不过，原因是选取了[0]情况下，不能同时选择[2]和[9]
        return max(a, b, c)
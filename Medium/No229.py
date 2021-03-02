class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        看了部分答案，摩尔投票法，解决的是超过半数的票
        这里统计的是超过n/3的数字，其实差不多
        当统计栏里面有两个不同的数，新出现的数不在统计栏里时才进行抵消即可
        """
        if len(nums) <= 1:
            return nums
        iDict = {}
        for num in nums:
            if len(iDict) < 2:
            # 如果词典中不足两个数字
                iDict[num] = iDict[num] + 1 if num in iDict else 1
            elif len(iDict) == 2:
                if num in iDict:
                # 是统计栏里的一位选手
                    iDict[num] += 1
                else:
                # 是统计栏外的另一名选手，进行票数相消
                    for key, value in iDict.items():
                        iDict[key] = value -1
                        if iDict[key] == 0:
                        # 计数变为0了
                            del iDict[key]
        # 应当注意的是，当iDict中含有两名选手时，这样只可以保证这两名选手比其他人选票多，但是并不能保证这两名超过n/3了，例如[1,2,3,4],[3,2,3]
        temp = iDict.keys()
        # print iDict
        # if len(temp) <= 1:
        # # 只有一个元素时，此选手夺冠，没有元素时，无人满足
        #     return temp
        # if iDict[temp[0]] == iDict[temp[1]]:
        # # 两人并列第一名
        #     return temp
        # iDict[temp[0]], iDict[temp[1]] = 0, 0
        # # 将字典内计数归零
        for i in temp:
        # 将字典内计数归零
            iDict[i] = 0

        for num in nums:
            if num in iDict:
            # 只对这两名选手计数
                iDict[num] += 1 
        ans = []
        for i in temp:
            if iDict[i] > len(nums)/3:
                ans.append(i)
        return ans
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        """
        将本题转化为一个排序问题，设置一个特殊的函数用来定义两个数字的“大小”，使用了插入排序
        """
        # 用此函数来比较两个数字“大小”，若n1在前比n2在前组成的数字要大，则认为n1大
        def pk(n1, n2):
            s1 = n1 + n2
            s2 = n2 + n1
            if int(s1) >= int(s2):
                return True
            else:
                return False

        left, right = 1, len(nums)-1
        res = [str(nums[0])]
        # 遍历原数组
        while left <= right:
            # 比较当前数字的大小，找到合适位置插入到res中
            for i in range(0, left):
                if pk(str(nums[left]), res[i]) == True:
                    res.insert(i, str(nums[left]))
                    break
            else:
            # 当前数字比res中所有数都小，添加到res末尾
                res.append(str(nums[left]))
            left += 1
        print res
        res = "".join(res).lstrip('0')
        return res if(res!='') else '0'




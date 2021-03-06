class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        全部异或，以异或值二进位制中最后一个1为依据，对列表进行分组
        """
        yihuo = 0
        for num in nums:
            yihuo ^= num
        flag = 1
        while yihuo & flag == 0:
            flag <<= 1
        # 找到最后一位1，以此为依据进行分组，num&flag==1为a组，其他为b组
        
        a = b = 0
        for num in nums:
            if num & flag != 0:
                a ^= num
            else:
                b ^= num
        return [a,b]
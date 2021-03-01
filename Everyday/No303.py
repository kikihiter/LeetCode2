class NumArray(object):
    """
    记录一个累和数组
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumList = []
        a = 0
        for num in nums:
            a += num
            self.sumList.append(a)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sumList[j]
        return self.sumList[j] - self.sumList[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
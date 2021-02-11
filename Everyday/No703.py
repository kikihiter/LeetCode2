class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)[::-1]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.k > len(self.nums):
        # 当数据流中不够k个数时
            for i in range(len(self.nums)):
            # 插入val
                if val > self.nums[i]:
                    self.nums.insert(i, val)
                    return self.nums[-1]
            else:
            # 找不到比val小的数据，插入到末端
                self.nums.append(val)
                return val

        if val <= self.nums[self.k-1]:
        # 新进入的数据比第k大的数要小，不影响后续计算，直接跳过，返回上一次的值
            return self.nums[self.k-1]
        else:
        # 插入到数组中
            for i in range(self.k):
                if val > self.nums[i]:
                    self.nums.insert(i, val)
                    return self.nums[self.k-1]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idict = {}
        def robOth(n):
            if n in idict:
                return idict[n]
            if n < 2:
                if n == 0:
                    idict[0] = nums[0]
                else:
                    idict[1] = max(nums[0],nums[1])
                return idict[n]
            else:
                rob1 = nums[n] + robOth(n-2)
                rob2 = nums[n-1] if n==2 else nums[n-1] + robOth(n-3)
                idict[n] = max(rob1, rob2)
                return idict[n]
                
        if not nums:
            return 0
        return robOth(len(nums)-1)
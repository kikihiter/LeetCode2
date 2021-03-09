class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        升序，双指针
        2021/03/09
        """
        if not nums:
            return
        if len(nums) < 4:
            return sum(nums) 
        
        def numClosest(a, b):
        # 比较a与b，返回最接近target的数字，相同距离取较小数字
            if a == b:
                return a
            if a == target or b == target:
                return target
            
            if a > target and b > target:
                return min(a,b)
            elif a < target and b < target:
                return max(a,b)
            elif a < target and b >target:
                if target - a > b - target:
                    return b
                return a
            elif b < target and a >target:
                if target - b > a - target:
                    return a
                return b
            

        ans = float('inf')
        nums = sorted(nums)
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > target:
                    right -= 1
                elif s == target:
                    return target
                elif s < target:
                    left += 1
                ans = numClosest(ans, s)
        return ans

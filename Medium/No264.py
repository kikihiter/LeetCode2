class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        设数字为num = 2^a * 3^b * 5^c
        1   a   b   c
        2   1   0   0
        3   0   1   0
        4   2   0   0
        5   0   0   1
        6   1   1   0
        8   3   0   0
        9   0   2   0
        10  1   0   1
        12  2   1   0
        15  0   1   1
        16  4   0   0
        """
        if n == 1:
            return 1
        nums = [1]
        i = 0
        a = b = c = 0
        while len(nums) < n :
            if nums[a]*2 < nums[b]*3 and nums[a]*2 < nums[c]*5:
                nums.append(nums[a]*2)
                a += 1
            elif nums[b]*3 < nums[a]*2 and nums[b]*3 < nums[c]*5:
                nums.append(nums[b]*3)
                b += 1
            elif nums[c]*5 < nums[a]*2 and nums[c]*5 < nums[b]*3:
                nums.append(nums[c]*5)
                c += 1
            elif nums[a]*2 == nums[b]*3 and nums[a]*2 < nums[c]*5:
                nums.append(nums[a]*2)
                a += 1
                b += 1
            elif nums[a]*2 == nums[c]*5 and nums[a]*2 < nums[b]*3:
                nums.append(nums[a]*2)
                a += 1
                c += 1
            elif nums[b]*3 == nums[c]*5 and nums[b]*3 < nums[a]*2:
                nums.append(nums[b]*3)
                b += 1
                c += 1
            elif nums[a]*2 == nums[c]*5 == nums[b]*3:
                nums.append(nums[a]*2)
                a += 1
                b += 1
                c += 1
            # print nums,a,b,c
        return nums[-1]

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(numbers)-1):
            oth = target - numbers[i]
            if oth < numbers[i]:
                break
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            if oth in numbers[i+1:]:
                return [i+1, numbers[i+1:].index(oth)+i+2]
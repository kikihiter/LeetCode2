class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        n=len(numbers)
        l=0
        r=n-1
        while l<r:
            if numbers[l]+numbers[r]==target: return[l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r-=1
            else: l+=1
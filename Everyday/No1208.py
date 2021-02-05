class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        """
        先将各个位置字符的cost计算出来，存储在列表costList中。然后用双指针，使右指针从左向右不断遍历costList，满足条件继续遍历，不满足条件，左指针右移一位。最终左右指针之差即为最大长度。其中用一个costSum来计算两指针之间的cost和。
        """
        costList = []   # 记录各个位置变化的开销
        # 遍历两个字符串，将cost信息存入costList
        for i in range(len(s)):
            temp = ord(s[i]) - ord(t[i])
            if temp < 0:
            # 当为负值时，转为正
                temp = -temp
            costList.append(temp)
        
        left, right, costSum = 0, 0, 0
        while left<=right and right<len(s):
            costSum += costList[right]
            if costSum > maxCost:
            # 超限，left右移
                costSum -= costList[left]
                left += 1
            right += 1

        return right - left
                

        

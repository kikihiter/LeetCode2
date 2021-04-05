class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        210402
        分别从头和尾各遍历一次，用两个数组记录最大值
        """
        if not height or height == []:
            return 0
        leftHeight = [0 for _ in height]
        rightHeight = [0 for _ in height]
        maxHeight = -float('inf')
        leftHeightIndex, rightHeightIndex = 0, len(height)-1
        for i in range(len(height)):
            if height[i] < 0:
                height[i] = 0
            if height[i] > maxHeight:
                maxHeight = height[i]
                leftHeightIndex = i
            leftHeight[i] = maxHeight
        maxHeight = -float('inf')
        heSum = 0
        for i in range(len(height)-1,-1,-1):
            heSum += height[i]
            if height[i] > maxHeight:
                maxHeight = height[i]
                rightHeightIndex = i
            rightHeight[i] = maxHeight
        leftSum, rightSum = 0, 0
        for i in range(leftHeightIndex):
            leftSum += leftHeight[i]
        for i in range(rightHeightIndex+1,len(height)):
            rightSum += rightHeight[i]
        # print rightHeight, leftHeight, maxHeight,heSum,rightHeightIndex,leftHeightIndex
        return leftSum + rightSum + maxHeight*(rightHeightIndex - leftHeightIndex + 1) - heSum
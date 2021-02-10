class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        三指针
        维护一个窗口，使窗口中的不同整数个数为K
        left从左到右移动，对每一个left，找到满足条件的右端点，最近右端点为middle，最远右端点为right
        当窗口中不同整数个数n比K小时，向右移动middle
        n==K：right从middle开始向右移动
        n>K:右移一格left
        """
        left = middle = right = 0   # 三个指针
        n = 0   # 窗口内元素种类数目
        # 初始化窗口，使其中元素种类为K个，若不足K，直接返回0
        while left <= middle <= right < len(A):
            if A[middle] not in A[:middle]:
                n += 1
            if n == K:
                break
            middle += 1
            right = middle
        else:
            return 0
        ans = 0 # 此时窗口内为一个好子数组，ans用来记录好子数组个数
        while left <= middle < len(A):
            right = middle
            # 将right与middle对齐
            while right < len(A) and A[right] in A[left:middle+1]:
            # 找到最远的right，其中每次循环，窗口内的子数组都是好子数组
                ans += 1
                right += 1
            right = middle  # 重新与middle对齐
            if A[left] not in A[left+1:middle+1]:
            # 窗口左端与窗口中的其他元素都不相同
                while right < len(A) and A[right] in A[left+1:middle+1]:
                # 找到另一个与窗口中元素不同的点
                    right += 1
                if right == len(A):
                # 找不到符合条件的右端点了，后面已经没有好子数组了，直接跳出循环
                    break
                middle = right  # 新的middle
            left += 1   # 右移left点
            middle = max(middle,left)   # 避免middle比left从而跳出循环
        return ans
        

                    

        

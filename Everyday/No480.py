class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        """
        对窗口内的数字排序，找出中位数
        """
        if k<2:
            return nums
        label = nums[:k]   # 窗口
        label.sort()
        # print label
        if k&1 == 1:
        # k为奇数
            a = label[k>>1]
        else:
        # k为偶数
            a = float(label[(k>>1)-1] + label[k>>1])/2
        ans = [a]
        
        for i in range(len(nums)-k):
        # 移动窗口
            label.remove(nums[i])   # 移动后将前面的数字排出窗口
            for j in range(k-1):
            # 将后一位数字添加进窗口
                if nums[i+k] < label[j]:
                # 按大小插入进窗口
                    label.insert(j,nums[i+k])
                    break
            else:
                label.append(nums[i+k])
            # print label
            if k&1 == 1:
            # k为奇数
                a = label[k>>1]
            else:
            # k为偶数
                a = float(label[(k>>1)-1] + label[k>>1])/2
                # print a
            ans.append(a)
        return ans

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            return 2 if (arr[0] != arr[1]) else 1
        flag, l, maxl= 0, 0, 0  # 记录上一个符号（-1代表上一个符号为小于号，0代表等号，1代表大于号），当前长度，最长长度
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                if flag == 0:
                # 上一个为等号
                    flag = -1
                    l += 1
                    maxl = max(maxl, l)
                    continue
                elif flag == 1:
                # 上一个是大于号
                    flag = -1
                    l += 1
                    maxl = max(maxl, l)
                    continue
                elif flag == -1:
                # 上一个是小于号
                    maxl = max(maxl, l)
                    l = 1
                    continue
            elif arr[i-1] == arr[i]:
                flag = 0
                maxl = max(maxl, l)
                l = 0
                continue
            elif arr[i-1] > arr[i]:
                if flag == 0 or flag == -1:
                    flag = 1
                    l += 1
                    maxl = max(maxl, l)
                    continue
                else:
                    maxl = max(maxl, l)
                    l = 1
                    continue
        return maxl+1



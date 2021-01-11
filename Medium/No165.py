class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 用'.'来切割字符串，形成列表
        v1List = version1.split('.')
        v2List = version2.split('.')
        i = 0

        # 从每个列表的第一位开始比较，一直到其中一个列表结束
        while i < len(v1List) and i <len(v2List):
            v1 = v1List[i].lstrip('0')  # 去除前导0
            v1 = 0 if (v1=="") else int(v1) # 将字符串转化为整型
            v2 = v2List[i].lstrip('0')
            v2 = 0 if (v2=="") else int(v2)
            if v1 > v2:
            # v1大于v2，直接返回1
                return 1
            elif v1 < v2:
                return -1
            i += 1
        # 比较剩余序列
        while i <len(v1List):
            v1 = v1List[i].lstrip('0')
            v1 = 0 if (v1=="") else int(v1)
            # 若剩余序列不全为0，直接返回
            if v1>0:
                return 1
            i += 1
        while i <len(v2List):
            v2 = v2List[i].lstrip('0')
            v2 = 0 if (v2=="") else int(v2)
            if v2>0:
                return -1
            i += 1
        # 所有数字均比较完毕，未发现不同，返回0
        return 0
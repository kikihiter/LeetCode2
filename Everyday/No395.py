class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        用一个词典记录各个字母出现位置的索引
        """
        if len(s) == 0:
        # 长度为0时，直接返回
            return 0
        if k == 1:
            return len(s)
        charDict = {}
        for i in range(len(s)):
        # 记录所有字母索引信息
            if s[i] in charDict:
                charDict[s[i]].append(i)
            else:
                charDict[s[i]] = [i]
        temp = []
        for ch, charIndexList in charDict.items():
            if len(charIndexList) < k:
            # 数量不足k的字母单独拿出来
                temp.extend(charIndexList)
                # print "ch", ch, temp
        temp = sorted(temp)
        # print "temp=", temp
        if len(temp) == 0:
        # 没有不符合要求的字母，直接返回字符串长度
            return len(s)
        maxl = 0
        l = len(s)
        temp.append(l)
        temp.insert(0,-1)
        # print "temp~=", temp
        for i in range(1, len(temp)):
            left, right = temp[i-1], temp[i]
            t = self.longestSubstring(s[left+1:right], k)
            # print "t", t, s[left+1:right]
            maxl = max(maxl, t)
            # print s,maxl
        return maxl
        
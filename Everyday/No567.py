class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        """
        用词典记录一段字符串中各个字母出现的次数，dict1记录s1，dict2记录当前窗口，cmp(dict1,dict2) == 0时，返回True
        """
        dict1, dict2 = {}, {}
        if len(s1) > len(s2):
        # s1比s2长，直接返回False
            return False
        for i in range(len(s1)):
            if s1[i] in dict1:
                dict1[s1[i]] += 1
            else:
                dict1[s1[i]] = 1
            if s2[i] in dict2:
                dict2[s2[i]] += 1
            else:
                dict2[s2[i]] = 1
        if cmp(dict1, dict2) == 0:
            return True
        l = len(s1)
        for j in range(len(s2)-len(s1)):
            print j
            if dict2[s2[j]] == 1:
                del dict2[s2[j]]
            else:
                dict2[s2[j]] -= 1
            if s2[j+l] in dict2:
                dict2[s2[j+l]] += 1
            else:
                dict2[s2[j+l]] = 1
            if cmp(dict1, dict2) == 0:
                return True
        
        return False


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        一共26个英文字母，统计出每个字母出现的位置。单独对各字母进行处理。
        """
        # 最大为len(s)
        if k > len(s)-2:
            return len(s)
        # print ord(s[0]) - 65
        chaList = []    # 用于记录各个字母信息的列表
        for j in range(26):
            chaList.append([])   # 初始化
        for i in range(len(s)): # 读取信息
            chaList[ord(s[i])-65].append(i)
        # print chaList
        maxL = k    # 最长长度最小为k
        for chara in chaList:
            if chara == []:
            # chara为空意味着s中不存在此字母，直接跳过
                continue
            while chara != []:
                t = k
                for m in range(len(chara)):
                # chara[0] + t是最远能够到达的位置
                    if chara[m] <= chara[0] + t:
                        t+=1
                    else:
                    # 最远的位置到达不了当前位置
                        break
                else:
                # 当前列表所有位置都到达了
                    t = min(t,len(s))
                maxL = max(maxL,t)
                if maxL == len(s):
                # 最长长度到达字符串s长度，直接返回字符串长度
                    return maxL
                chara.pop(0)
        return maxL
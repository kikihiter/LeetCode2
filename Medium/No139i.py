class Solution(object):
    def __init__(self):
        self.visited = []

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 在字典中，直接返回True
        if s in wordDict:
            return True
        # 遍历字符串
        for i in range(len(s)):
            # 当前i个字母可以组成单词时
            if s[:i+1] in wordDict:
                # 当列表中有这段字符串时，则代表这一段不能被分割
                if s[i+1:] in self.visited:
                    continue
                flag = self.wordBreak(s[i+1:], wordDict)
                # 未成功时，将失败字符串存入列表中
                if flag == False:
                    self.visited.append(s[i+1:])
                else:
                    return True
        return False
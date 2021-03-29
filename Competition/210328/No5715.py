class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        """
        210328
        做一个词典
        """
        iDict = {}
        for iKey, iValue in knowledge:
            iDict[iKey] = iValue
        ss = ""
        word = ""
        isKey = False
        for letter in s:
            if letter == '(':
                isKey = True
                continue
            elif letter == ')':
                if word in iDict:
                    ss += iDict[word]
                else:
                    ss += '?'
                word = ""
                isKey = False
                continue    
            if isKey == True:
                word += letter
            else:
                ss += letter
        return ss
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        temp = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                temp.append(s1[i])
                temp.append(s2[i])
                if len(temp) > 4:
                    return False
        if len(temp) == 0:
            return True
        
        if len(temp) != 4:
            return False
        return temp[0] == temp[3] and temp[1] == temp[2]
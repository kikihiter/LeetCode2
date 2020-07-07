class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        row = [1,1]
        
        while rowIndex != 1:
            newr = [1]
            for i in range(1, len(row)):
                newr.append(row[i] + row[i-1])
            newr.append(1)
            row = newr
            rowIndex -= 1
        return row
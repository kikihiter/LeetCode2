        re = []
        if numRows == 0:
            return re
        re.append([1])
        if numRows == 1:
            return re
        re.append([1,1])
        if numRows == 2:
            return re
        
        while numRows != 2:
            if re == []:
                temp = [1]
            else:
                temp = re[-1]
            newl = [1]
            for i in range(1,len(temp)):
                newl.append(temp[i] + temp[i-1])
            newl.append(1)
            re.append(newl)
            numRows -= 1
        
        return re
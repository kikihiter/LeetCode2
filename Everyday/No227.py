class Solution(object)
    def calculate(self, s)
        
        type s str
        rtype int
        
        
        应该是不存在括号的
        先遍历一遍，处理字符串中的乘法和除法，用一个栈来记录其他信息
        再遍历栈中信息，处理加法和减法
        210311
        
        i = 0
        stack = []
        while i  len(s)
            char = s[i]
            if char == ' '
            # 空格，跳过
                i += 1
            elif char == '+' or char == '-' or char == '' or char == ''
            # 运算法则，直接入栈
                stack.append(char)
                i += 1
            else
                num = 0
                while i  len(s) and 48 = ord(s[i]) = 57
                    num = num10 + int(s[i])
                    i += 1
                if stack != []
                # 栈中不为空时
                    if stack[-1] == ''
                        stack.pop(-1)
                        preNum = stack.pop(-1)
                        num = preNumnum
                    elif stack[-1] == ''
                        stack.pop(-1)
                        preNum = stack.pop(-1)
                        num = preNumnum
                stack.append(num)

        ans = 0
        sign = 1
        print stack
        for letter in stack
            if letter == '+'
                sign = 1
            elif letter == '-'
                sign = -1
            else
                print sign,letter
                ans += sign  letter
        return ans
            
            

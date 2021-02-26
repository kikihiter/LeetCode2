class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        """
        用长为26的二进制表示单词，每一个位置对应一个字母，用0表示不含此字母，1表示含有（1个及1个以上）,[z,y,x...a]
        false if (puzzle^word)&puzzle^(puzzle^word) != 0 
        => (puzzle|word)^puzzle !=0
        例：puzzle = 0011010100; 头字母数字charNum = 0000010000; word = 0010010101
            word & charNum = 0000010000 (!=0意味着包含头字母)
            puzzle|word = 0011010101 (puzzle和word字母并集)
            (puzzle|word)^puzzle = 0000000001 (!=0意味着单词word中有额外的字母不在puzzle中)
        """
        """
        为缩短字母转化为数字的时间，用一个含有26个元素的词典来记录字母与数字的对应关系
        """
        """
        还是超时，看了答案，重新写一个
        """
        # char2num = {}
        # for i in range(26):
        #     num = 1
        #     for _ in range(i):
        #         num <<= 1
        #         # 将1移动到对应位置
        #     char2num[chr(i+97)] = num
        
        # def word2num(word):
        # # 将word转化为num
        #     temp = []
        #     num = 0
        #     for ch in word:
        #         if ch not in temp:
        #             temp.append(ch)
        #             # 不重复添加
        #             num += char2num[ch]
        #     return num
        
        # def puzzle2num(puzzle):
        # # 将puzzle转化为num
        #     """
        #     rtype: touple(int, int) 第一个整型是puzzle头字母的数字表示，第二个是puzzle整个单词的数字表示
        #     """
        #     num1 = num2 = 0
        #     for ch in puzzle:
        #         if num1 == 0:
        #         # 未设置头字母时
        #             num1 = char2num[ch]
        #         num2 += char2num[ch]
        #         # 数字整个单词的数字表示
        #     return (num1, num2)

        # wordNum = [word2num(word) for word in words]
        # puzzleNum = [puzzle2num(puzzle) for puzzle in puzzles]
        # ans = []
        # for charNum, puzzle in puzzleNum:
        #     n = 0
        #     for word in wordNum:
        #         if word & charNum != 0:
        #         # word包含puzzle的头字母
        #             if (puzzle|word)^puzzle == 0:
        #                 n += 1
        #     ans.append(n)
        # return ans

        """
        淦tn一炮!
        """
        char2num = {}   # 字母与数字的对应关系
        for i in range(26):
            num = 1
            for _ in range(i):
                num <<= 1
                # 将1移动到对应位置
            char2num[chr(i+97)] = num
        num2n = {}  # 记录此数字出现的次数
        
        def doWord(word):
        # 处理word的函数，将当前word转化为数字表示，并在num2n中累加
            temp = []
            num = 0
            for ch in word:
                if ch not in temp:
                    temp.append(ch)
                    # 不重复添加
                    num += char2num[ch]
            if len(temp) > 7:
                return
            num2n[num] = num2n[num] + 1 if num in num2n else 1
            return
        
        def doPuzzle(puzzle):
        # 处理puzzle的函数
            puzzleNum = []  # 存储对应位置的由数字表示的字母
            n = 0   # 计数
            for ch in puzzle:
            # 将数字存储入数组
                puzzleNum.append(char2num[ch])
            for i in range(64):
            # 穷举，锁定开头字母的情况下，剩下6个字母，每个字母有存在或者不存在两种状态，则一共有64种情况，分别可以由6位二进制来表示
                num = 0 # 数字用于累加
                for j in range(6):
                # 6位二进制，用j来表示对应位置
                    a = (i>>j)&1    # a即为i在j位的数字，不是0就是1
                    num += puzzleNum[-j-1]*a    # num累加，对应的字母可能存在也可能不存在
                num += puzzleNum[0] # 加上首字母的数字表达
                n += num2n[num] if num in num2n else 0  # n计数
            return n
            
        [doWord(word) for word in words]
        return [doPuzzle(puzzle) for puzzle in puzzles]
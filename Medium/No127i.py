class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 当结束词不在字典中时，返回0
        if endWord not in wordList:
            return 0
        neighbor = {}   # 临近的词表
        # 对字典中的词做预处理
        for word in wordList:
            # 对每个字母做遮罩
            for i in range(len(word)):
                if i < len(word)-1:
                    wordMask = word[0:i] + "*" + word[i+1:]
                elif i == len(word)-1:
                    wordMask = word[0:i] + "*"
                # wordMask为生成的遮罩词
                # 添加word到遮罩词对应的词表中
                if wordMask in neighbor:
                    neighbor[wordMask].append(word)
                elif wordMask not in neighbor:
                    neighbor[wordMask] = [word]
        # print "预处理完毕"

        """
        # 单向广度优先遍历，会超时，逻辑应该没有问题(做完后发现有问题，问题在于可能会有重复的词进入队列，单靠屏蔽遮罩词无法屏蔽掉已经处理过的词，例如对中间词hot进行遮罩，*ot,h*t,ho*,会分别增加3次hot进入队列)
        wordQueue = [(beginWord, 1)]  # 处理word的队列，前面是待处理的单词，后面的数字表示已经经历过的转化次数+1（返回的是转化序列长度，beginWord也算作一个）
        haveRead = []   # 用于判断是否处理过此单词，将处理过的单词添加到此队列中
        # 当队列不为空时
        while wordQueue != []:
            word, num = wordQueue.pop(0)
            # 生成遮罩词
            for i in range(len(word)):
                if i < len(word)-1:
                    wordMask = word[0:i] + "*" + word[i+1:]
                elif i == len(word)-1:
                    wordMask = word[0:i] + "*"
                # 当wordMask已经处理过时，直接跳过，防止出现死循环
                if wordMask in haveRead:
                    continue
                if wordMask in neighbor:
                    # 如果结束词在遮罩词列表中，则意味着再转化一次就可以成功了
                    if endWord in neighbor[wordMask]:
                        return num+1
                    else:
                        for wordNei in neighbor[wordMask]:
                            wordQueue.append((wordNei, num+1)) 
                haveRead.append(wordMask)
        """
        # 看起来是铁了心了，一定让我们用双向广度优先遍历
        """
        # 实际写完后发现，比单向考虑的东西要多一些，主要集中在相遇情形的分析。
        # 首先一定会相遇，因为不可能越过其中某个集合而直接抵达后序的单词。A->B,D->C，B无法绕过C直接抵达D，因为所有与D相关的词在C中。
        # 理想的相遇情况，应该是wordMask1 == wordMask2,则两个词可以相互转换，返回num1+num2+1即可
        # 其次相遇可能存在延迟，导致得出的结论并不是最短的。
        # [hit]->[hot]->[dot], [cog]->[dog, log]->[dot,log]，这个时候其实已经转换完成了。
        """
        wordQueue1, wordQueue2 =  [(beginWord, 1)], [(endWord, 0)]  # 两个队列 
        haveRead1, haveRead2 = [], []   # 用来判断遮罩词是否处理过
        passWord1, passWord2 = {beginWord:1}, {endWord:0}   # 用来存储已经处理过的词，并记录运算到此词时经过的转化信息
        # 当两个队列不同时为空时（若有一个为空，则意味着无法转化）
        while wordQueue1 != [] and wordQueue2 != []:
            # print wordQueue1, wordQueue2
            word1, num1 = wordQueue1.pop(0)
            word2, num2 = wordQueue2.pop(0)
            # 对第i位字母进行遮罩等处理
            for i in range(len(word1)):
                if i < len(word1)-1:
                    wordMask1 = word1[0:i] + "*" + word1[i+1:]
                    wordMask2 = word2[0:i] + "*" + word2[i+1:]
                elif i == len(word1)-1:
                    wordMask1 = word1[0:i] + "*"
                    wordMask2 = word2[0:i] + "*"
                # 获得遮罩词
                # 理想的相遇情况，再进行一次转化即可完成操作
                if wordMask1 == wordMask2:
                    print num1, num2
                    return num1 + num2 + 1
                # 当遮罩词未处理过，并在预处理的词典中（意味着有相近的词）时
                if wordMask1 not in haveRead1 and wordMask1 in neighbor:
                    # 对预处理词典中的词（当前词相近的词）进行处理
                    for wordNei in neighbor[wordMask1]:
                        # 当此词已被反向处理过时，已经相遇
                        if wordNei in passWord2:
                            return num1 + passWord2[wordNei] + 1
                        # 此词未被前向处理过
                        if wordNei not in passWord1:
                            wordQueue1.append((wordNei, num1+1))
                            passWord1[wordNei] = num1 + 1
                haveRead1.append(wordMask1)
                # 参考前次
                if wordMask2 not in haveRead2 and wordMask2 in neighbor:
                    for wordNei in neighbor[wordMask2]:
                        if wordNei in passWord1:
                            return num2 + passWord1[wordNei] + 1
                        if wordNei not in passWord2:
                            wordQueue2.append((wordNei, num2+1))
                            passWord2[wordNei] = num2 + 1
                haveRead2.append(wordMask2)
        # 无法相遇，则无法转换，返回0
        return 0
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        """
        kiki 20200716
        test data:  [[1,3], [0,2], [1,3], [0,2]]        #True
                    [[1,2,3], [0,2], [0,1,3], [0,2]]    #False
                    [[4],[],[4],[4],[0,2,3]]    #非连通图 True
        """
        if len(graph)<2:
            return True
        # 小于等于两个点时，直接返回True

        graphA = [0]
        graphB = []     #设置两个列表，分别存储两个子集
        spotHaveRead = []       #设置列表，用于存储图中已经遍历过的点
        while len(spotHaveRead) != len(graph):      #当仍有点没有被遍历时，循环
            graphAPlus, graphBPlus = False, False       
            #设置两个flag，用来判断AB两个集合是否有新增加的点。本题中的图，不一定连通。
            for spot in graphA:
            #遍历集合A中的点
                if spot in spotHaveRead:
                #如果已经遍历过，则直接跳过
                    continue
                for spotConnect in graph[spot]:
                #对于此时正在操作的点spot，它的相连点为spotConnect，对每一个相连点进行操作
                    if spotConnect in graphA:
                    #spot的一个相邻点在集合A中，因为spot也在A中，为非二分图
                        return False
                    if spotConnect in graphB:
                        continue    
                    
                    #相连点既不在A中也不在B中，则将相连点添加到B中（因为spot在A中）
                    graphB.append(spotConnect)
                    graphBPlus = True
                    #B中添加了新的点，则将flag改为True
                spotHaveRead.append(spot)
                #将遍历过的点添加到集合中

            #类似上述操作
            for spot in graphB:
                if spot in spotHaveRead:
                    continue
                for spotConnect in graph[spot]:
                    if spotConnect in graphB:
                        return False
                    if spotConnect in graphA:
                        continue
                    graphA.append(spotConnect)
                    graphAPlus =True
                spotHaveRead.append(spot)
            
            #当AB中有新添加的点时，越过下述步骤
            if graphAPlus == False and graphBPlus == False:
            #两个flag都为False，也就是AB中都没有新增加的点
                for i in range(len(graph)):
                    if i not in spotHaveRead:
                        #选取图中一个没有读取过的点，将其添加到A中
                        graphA.append(i)
                        break
                        
        #图中全部点分配完成，未出现矛盾，则二分图成立
        return True
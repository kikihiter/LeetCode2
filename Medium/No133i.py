"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        """
        1.用队列nodeQueue存储node，将与node相邻的点存入队列；
        2.存入时，需要防止重复存入，即已经存入过的点不再存入，因为是无向图，1->2，则2->1，用列表haveRead存储已经读取过的点，每次存入队列时与此列表进行对比，未在列表中的点进入队列并存储入列表，在列表中的点，直接跳过；
        3.克隆正在处理的节点的邻居属性给新节点，用一个词典newNode来存储新生成的各个节点，若当前节点未在newNode中，则新生成节点，并存储入词典中，对邻居节点也是如此处理，这样可以保证生成的是一个图
        4.队列nodeQueue为空时，跳出
        """
        if not node:
            return
        nodeQueue = [node]  # 存储未处理的点
        haveRead, newNode = [], {}  # 一个用来判断是否重复处理，一个用来存储新生成节点的val信息
        # 当队列不为空，即仍有节点未处理时
        while nodeQueue != []:
            node = nodeQueue.pop(0)
            # 当当前处理节点已被生成过时，直接提取
            if node.val in newNode:
                nodeN = newNode[node.val]
            # 当当前处理节点未被复制val信息时，生成一个新的点，值为node.val，存储入词典中
            if node.val not in newNode:
                nodeN = Node(node.val)
                newNode[node.val] = nodeN
            # 当前节点的邻居为待处理节点，存储入nodeQueue中（不要重复的）
            for neigh in node.neighbors:
                # 当邻居节点曾经生成过时，直接读取邻居节点
                if neigh.val in newNode:
                    nodeNei = newNode[neigh.val]
                # 当未曾生成过时，生成一个新的节点
                if neigh.val not in newNode:
                    nodeNei = Node(neigh.val)
                    newNode[neigh.val] = nodeNei
                # 当此邻居节点未被添加至新节点的邻居节点列表中时，进行添加，防止重复添加，虽然应该不会重复
                if nodeNei not in nodeN.neighbors:
                    nodeN.neighbors.append(nodeNei)
                # 当邻居节点未被处理过时，添加至处理队列中               
                if neigh.val not in haveRead:
                    nodeQueue.append(neigh)
            # 当前节点已被处理，添加至列表haveRead中
            haveRead.append(node.val)
        return newNode[1]
            


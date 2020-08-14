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
        if not node:
            return None
        _map = {}
        for key, val in self.dfs(node,_map).items():
            val.neighbors = [_map[x] for x in key.neighbors]
        return _map[node]
            
    def dfs(self,node,map):
        if node not in map:  # 如果在map里，就说明已经遍历复制了，返回map即可
            map[node] = Node(node.val,None)
            for i in node.neighbors:
                self.dfs(i,map)
        return map

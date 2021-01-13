# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
本人的解法实际上并不符合题意，我只是先把题做出来，没想到通过了编译
功能上可以满足要求，但是我会改变给定二叉树的结构，事实上，最后二叉树让我删干净了
空间上，没有使用额外空间
时间上，next()的时间复杂度这里不好计算，处于O(1)到O(h)之间
"""
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        temp = self.root
        # print temp
        leftNode = temp.left
        if leftNode == None:
            minVal = self.root.val
            self.root = self.root.right
            return minVal
        while leftNode.left != None:
            temp = leftNode
            leftNode = leftNode.left
        minVal = leftNode.val
        if leftNode.right != None:
            temp.left = leftNode.right
        else:
            temp.left = None
        return minVal
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.root == None:
            return False
        return True



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
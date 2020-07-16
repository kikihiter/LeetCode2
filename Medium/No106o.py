
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(left,right):
            if left>right:
                return
            val=postorder.pop()
            root=TreeNode(val)
            idx=hashmap[val]
            root.right=helper(idx+1,right)
            root.left=helper(left,idx-1)
            
            return root

        hashmap={val:idx for idx, val in enumerate(inorder)}
        return helper(0,len(inorder)-1)
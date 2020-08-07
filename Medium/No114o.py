class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
难受，我发现我之前误解了答案的意思，我以为他说的“前驱节点”就是最终的前驱节点（也就是左子树前序遍历的最后一个点），实际上不是，它只是暂时的（是左子树的最右节点），在后序的处理过程中，慢慢化为最终形态。
例如输入这个二叉树[1,2,4,3]
          1
      2      4
   3   *   *   *
答案的解法：
          1
      2      *
   3   4   *   *
 —————— 
          1
      *      2
   *   *   3   4
 ——————
          1
      *      2
   *   *   3   *
 * * * * * 4 * * 
——————
          1
      *      2
   *   *   *   3
 * * * * * * * 4
我的解法：
          1
      2      *
   3   *   *   *
 * 4 * * * * * * 
——————
          1
      *      2
   *   *   3   *
 * * * * * 4 * *
—————— 
          1
      *      2
   *   *   *   3
 * * * * * * 4 *
——————
          1
      *      2
   *   *   *   3
 * * * * * * * 4  

 
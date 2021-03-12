class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        """
        "o,#,#"
        "o,o,#,#,#"
        "o,#,o,#,#"
        "o,o,#,#,o,#,#"
        "o,o,o,#,#,#,#"
        "o,o,#,o,#,#,#"
        "o,#,o,o,#,#,#"
        "o,#,o,#,o,#,#"
        "9,3,4,#,#,1,#,#,2,#,6,#,#"
        "9,3,4,#,#,1,#,#,2,#,#"
        "9,3,4,#,#,1,#,#,#"
        "9,#,#"
        对于每一个叶子节点，其序列号的表达式一定是o##的形式，替换每一个o##为#，不断摘除叶子节点，判断是否正确
        """
        if ',' in preorder:
        # 预处理，去除字符串中的','，并将数字替换掉
            preorder = preorder.split(',')
            for i, letter in enumerate(preorder):
                if letter != '#':
                    preorder[i] = 'O'
            preorder = ''.join(preorder)

        if len(preorder)%2 == 0:
        # 正常的序列长度不能被2整除，因为#的数目一定比数字多一个
            return False
        if preorder == "#":
        # 全部叶子节点都被摘除了，只剩#
            return True
        if preorder[0] == '#':
        # 第一个字符为#，根节点为空，却还有其他节点，不可能
            return False
        ans = ""
        i = 0
        while i < len(preorder)-2:
            if preorder[i] != '#' and preorder[i+1] == '#' and preorder[i+2] == '#':
            # 找到叶子节点，替换成'#'
                i += 3
                ans += '#'
                continue
            ans += preorder[i]
            i += 1
        while i < len(preorder):
            ans += preorder[i]
            i += 1
        if ans == preorder:
        # ans和preorder相同，证明其中没有叶子节点，显然不可能
            return False
        
        return self.isValidSerialization(ans)
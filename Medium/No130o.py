class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        n, m = len(board), len(board[0])
        que = collections.deque()
        for i in range(n):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
        for i in range(m - 1):
            if board[0][i] == "O":
                que.append((0, i))
            if board[n - 1][i] == "O":
                que.append((n - 1, i))
        
        while que:
            x, y = que.popleft()
            board[x][y] = "A"
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    que.append((mx, my))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/surrounded-regions/solution/bei-wei-rao-de-qu-yu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# 大体思路和自己写的差不多，都是先找到所有未被包围的“O”，然后将其他的“O”改为“X”。
# 答案里的处理比我的要聪明很多，直接利用原矩阵，将外围“O”先改为“A”，省了很多空间和时间。
"""
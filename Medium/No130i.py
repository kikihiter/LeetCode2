class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 当两行以内时，直接返回
        if len(board) < 3:
            return
        # 当两列以内时，直接返回
        if len(board[0]) < 3:
            return
        oQueue, oList = [], []  # oQueue作为队列用来存储未处理的外围O点，oList用来存储外围O点，即未被围住的点
        ml, nl = len(board), len(board[0])
        # 读取第一排以及最后一排信息，并存储为O的点
        for j in range(nl):
            # 第一排
            if board[0][j] == "O":
                oQueue.append((0, j))
                oList.append((0, j))
            # 最后一排
            if board[ml-1][j] == "O":
                oQueue.append((ml-1, j))
                oList.append((ml-1, j))
        # 读取第一列以及最后一列信息（掐头去尾，防止重复），并存储
        for i in range(1, ml-1):
            # 第一列
            if board[i][0] == "O":
                oQueue.append((i, 0))
                oList.append((i, 0))
            # 最后一列
            if board[i][nl-1] =="O":
                oQueue.append((i, nl-1))
                oList.append((i, nl-1))
        # 从边界上的点向内延伸，将未被围住的点记录下来
        while oQueue != []:
            m, n = oQueue.pop(0)
            # 在边界上的
            if m == 0:
                if (m+1, n) not in oList and board[m+1][n] == "O":
                    oQueue.append((m+1, n))
                    oList.append((m+1, n))
                continue
            if m == ml-1:
                if (m-1, n) not in oList and board[m-1][n] == "O":
                    oQueue.append((m-1, n))
                    oList.append((m-1, n))
                continue
            if n == 0:
                if (m, n+1) not in oList and board[m][n+1] == "O":
                    oQueue.append((m, n+1))
                    oList.append((m, n+1))
                continue
            if n == nl-1:
                if (m, n-1) not in oList and board[m][n-1] == "O":
                    oQueue.append((m, n-1))
                    oList.append((m, n-1))
                continue
            # 不在边界上的
            if (m+1, n) not in oList and board[m+1][n] == "O":
                oQueue.append((m+1, n))
                oList.append((m+1, n))
            if (m-1, n) not in oList and board[m-1][n] == "O":
                oQueue.append((m-1, n))
                oList.append((m-1, n))
            if (m, n+1) not in oList and board[m][n+1] == "O":
                oQueue.append((m, n+1))
                oList.append((m, n+1))
            if (m, n-1) not in oList and board[m][n-1] == "O":
                oQueue.append((m, n-1))
                oList.append((m, n-1))
        # 遍历将不在列表中的O点全部变为X
        for i in range(ml):
            for j in range(nl):
                if board[i][j] == "O" and (i, j) not in oList:
                    board[i][j] = "X"

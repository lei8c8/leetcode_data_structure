class Solution:
    def candyCrush(self, board):
        m, n = len(board), len(board[0])

        def find():
            to_be_crushed = set()
            for i in range(1, m - 1):
                for j in range(n):
                    if board[i][j] == 0:
                        continue
                    if board[i][j] == board[i - 1][j] and board[i][j] == board[i + 1][j]:
                        to_be_crushed.add((i - 1, j))
                        to_be_crushed.add((i, j))
                        to_be_crushed.add((i + 1, j))
            for i in range(m):
                for j in range(1, n - 1):
                    if board[i][j] == 0:
                        continue
                    if board[i][j] == board[i][j - 1] and board[i][j] == board[i][j + 1]:
                        to_be_crushed.add((i, j - 1))
                        to_be_crushed.add((i, j))
                        to_be_crushed.add((i, j + 1))
            return to_be_crushed

        def crush(crush_set):
            for i, j in crush_set:
                board[i][j] = 0

        def drop():
            for j in range(n):
                last_zero_idx = -1
                for i in range(m - 1, -1, -1):
                    if board[i][j] == 0:
                        last_zero_idx = max(last_zero_idx, i)
                    if board[i][j] != 0:
                        if last_zero_idx >= 0:
                            board[i][j], board[last_zero_idx][j] = board[last_zero_idx][j], board[i][j]
                            last_zero_idx -= 1

        s = find()
        while s:
            crush(s)
            drop()
            s = find()
        return board



        
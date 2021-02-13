class Solution:
    def __init__(self):
        self.row_cnt = None
        self.col_cnt = None

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.row_cnt = len(board)
        self.col_cnt = len(board[0])

        is_break = self.break_candy(board)
        self.drop_candy(board)

        return is_break and self.candyCrush(board) or board


    def break_candy(self, board):
        is_break = False
        for r in range(self.row_cnt):
            for c in range(self.col_cnt - 2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    is_break = True

        for c in range(self.col_cnt):
            for r in range(self.row_cnt - 2):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    is_break = True
        return is_break

    def drop_candy(self, board):
        for c in range(self.col_cnt):
            to_wr = self.row_cnt - 1
            for r in range(self.row_cnt-1, -1, -1):
                if board[r][c] > 0:
                    board[to_wr][c] = board[r][c]
                    to_wr -= 1

            for r in range(to_wr, -1, -1):
                board[r][c] = 0
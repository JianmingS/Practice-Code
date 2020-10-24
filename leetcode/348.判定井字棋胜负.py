class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.chessboard = [[0]*n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.chessboard[row][col] = player

        if self._is_vertical_legal(row, col):
            return player

        if self._is_horizontal_legal(row, col):
            return player

        if self._is_diagonal_left_to_right(row, col):
            return player

        if self._is_diagonal_right_to_left(row, col):
            return player

        return 0

    def _is_diagonal_right_to_left(self, row, col):
        if row + col != self.n - 1:
            return False

        player = self.chessboard[row][col]

        tmp_row = row - 1
        tmp_col = col + 1
        while tmp_row >= 0 and tmp_col < self.n:
            if self.chessboard[tmp_row][tmp_col] != player:
                return False
            tmp_row -= 1
            tmp_col += 1

        tmp_row = row + 1
        tmp_col = col - 1
        while tmp_row < self.n and tmp_col >= 0:
            if self.chessboard[tmp_row][tmp_col] != player:
                return False
            tmp_row += 1
            tmp_col -= 1

        return True

    def _is_diagonal_left_to_right(self, row, col):
        if row != col:
            return False

        player = self.chessboard[row][col]

        tmp_row = row - 1
        while tmp_row >= 0:
            if self.chessboard[tmp_row][tmp_row] != player:
                return False
            tmp_row -= 1

        tmp_row = row + 1
        while tmp_row < self.n:
            if self.chessboard[tmp_row][tmp_row] != player:
                return False
            tmp_row += 1

        return True

    def _is_horizontal_legal(self, row, col):
        player = self.chessboard[row][col]

        tmp_row = row - 1
        while tmp_row >= 0:
            if self.chessboard[tmp_row][col] != player:
                return False
            tmp_row -= 1

        tmp_row = row + 1
        while tmp_row < self.n:
            if self.chessboard[tmp_row][col] != player:
                return False
            tmp_row += 1

        return True

    def _is_vertical_legal(self, row, col):
        player = self.chessboard[row][col]

        tmp_col = col - 1
        while tmp_col >= 0:
            if self.chessboard[row][tmp_col] != player:
                return False
            tmp_col -= 1

        tmp_col = col + 1
        while tmp_col < self.n:
            if self.chessboard[row][tmp_col] != player:
                return False
            tmp_col += 1

        return True

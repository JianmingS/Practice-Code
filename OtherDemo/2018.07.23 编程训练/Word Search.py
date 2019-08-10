"""
https://leetcode.com/problems/word-search/description/
DFS
"""


class Solution(object):
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited = None

    def search(self, board, word, node, pos):
        x = node[0]
        y = node[1]
        if board[x][y] == word[pos]:
            if pos == len(word) - 1:
                return True
            for dir in self.direction:
                next_x = x + dir[0]
                next_y = y + dir[1]
                if next_x >= 0 and next_x < len(board) and next_y >= 0 and next_y < len(board[0]) and not self.visited[next_x][next_y]:
                    self.visited[next_x][next_y] = True
                    if self.search(board, word, (next_x, next_y), pos + 1):
                        return True
                    self.visited[next_x][next_y] = False
        return False

    def exist(self, board, word):
        self.visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.visited[i][j] = True
                if self.search(board, word, (i, j), 0):
                    return True
                self.visited[i][j] = False
        return False

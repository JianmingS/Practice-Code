import collections
from typing import List
import bisect


class Solution:
    def __init__(self):
        self.mat = None
        self.row_cnt = None
        self.col_cnt = None
        self.prefix = None
        self.dp_sum = None

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        self.mat = mat
        self.row_cnt = len(mat)
        self.col_cnt = len(mat[0])

        self.init_prefix()
        # print (self.prefix)
        self.init_dp_sum(K)

        return self.dp_sum

    def init_prefix(self):
        self.prefix = [[0] * (self.col_cnt + 1)
                       for _ in range(self.row_cnt + 1)]
        for i in range(1, self.row_cnt + 1):
            for j in range(1, self.col_cnt + 1):
                self.prefix[i][j] = self.prefix[i-1][j] + self.prefix[i][j-1] \
                    - self.prefix[i-1][j-1] + self.mat[i-1][j-1]

    def init_dp_sum(self, k):
        self.dp_sum = [[0] * self.col_cnt for _ in range(self.row_cnt)]
        for i in range(self.row_cnt):
            for j in range(self.col_cnt):
                x_right = min(i+1+k, self.row_cnt)
                y_right = min(j+1+k, self.col_cnt)
                x_left = max(i+1-k-1, 0)
                y_left = max(j+1-k-1, 0)
                self.dp_sum[i][j] = \
                    self.prefix[x_right][y_right] \
                    - self.prefix[x_left][y_right] \
                    - self.prefix[x_right][y_left] \
                    + self.prefix[x_left][y_left]


if __name__ == "__main__":
    pass

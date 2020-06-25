import collections
from typing import List
import bisect


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] = max(p[i] - dp[i+1][j], p[j] - dp[i][j-1])
        dp = [[0] * (len(piles) + 1) for _ in range(len(piles) + 1)]
        for i in range(len(piles) - 1, -1, -1):
            for j in range(i+1, len(piles)):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        # print (dp)
        return dp[0][len(piles) - 1] > 0


if __name__ == "__main__":
    pass

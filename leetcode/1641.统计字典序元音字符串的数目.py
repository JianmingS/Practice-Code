from functools import reduce


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0]*5 for i in range(n + 1)]
        dp[1] = [1] * 5

        for i in range(2, n+1):
            for j in range(0, 5):
                dp[i][j] = reduce(
                    lambda x, y: x+y,
                    [dp[i-1][m] for m in range(0, j+1)],
                    0
                )

        return reduce(lambda x, y: x+y, [dp[n][i] for i in range(5)], 0)

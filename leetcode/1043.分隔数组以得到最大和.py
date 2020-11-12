"""
dp[i] = dp[j] + max(array[j+1, i]) * (i - j)
i-k <= j <= i-1
"""


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [i > 0 and arr[i-1] or 0 for i in range(len(arr) + 1)]
        for i in range(len(arr) + 1):
            for j in range(i-1, (i-k-1) <= -1 and -1 or i-k-1, -1):
                dp[i] = max(dp[i], dp[j] + max(arr[j+1:i]) * (i-j))
        return dp[-1]

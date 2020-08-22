# 二维DP
class Solution: 
    def __init__(self):
        self.dp = None

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.dp = [[float('INF')]*110 for i in range(110)]
        self.s = s
        
        return self.solve(0, k)

    def solve(self, begin, k):
        if k < 0:
            return float('INF')
        
        if len(self.s) - begin <= k:
            return 0

        ans = self.dp[begin][k]
        if ans != float('INF'):
            return ans

        ans = self.solve(begin + 1, k-1)
        
        same = 0
        diff = 0
        str_len = 0
        for end in range(begin, len(self.s)):
            if self.s[begin] == self.s[end]:
                same += 1
                if same in [1, 2, 10, 100]:
                    str_len += 1
            else:
                diff += 1
                if diff > k:
                    break
            ans = min(ans, str_len + self.solve(end + 1, k - diff))
        
        self.dp[begin][k] = ans
        return ans                    
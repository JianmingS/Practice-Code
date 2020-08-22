#  四维DP
class Solution: 
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.s = s
        return self.solve(0, k, '', 0)

    @lru_cache(None)
    def solve(self, pos, k, pre_char, pre_char_length):
        if k < 0:
            return float('INF')

        if len(self.s) - pos <= k:
            return 0

        # delete pos char
        ans = self.solve(pos + 1, k-1, pre_char, pre_char_length)

        # keep pos char
        if self.s[pos] == pre_char:
            carry = (pre_char_length) in [1, 9, 99] and 1 or 0
            ans = min(
                ans,
                self.solve(pos + 1, k, pre_char, pre_char_length + 1) + carry
            )
        else:
            ans = min(
                ans,
                1 + self.solve(pos + 1, k, self.s[pos], 1)
            )

        return ans        

from itertools import combinations


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # return (n+4) * (n+3) * (n+2) * (n+1) // 24
        return len(list(combinations(range(n+5-1), (5-1))))

class Solution:
    def minFlips(self, target: str) -> int:
        current_status = '0'
        cnt = 0

        for ch in target:
            if ch == current_status:
                continue
            current_status = ch
            cnt += 1

        return cnt

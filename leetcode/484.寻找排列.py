class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ret = [i for i in range(1, len(s) + 2)]

        l = 0
        while l < len(s):
            if s[l] == 'I':
                l += 1
                continue

            r = l
            while r + 1 < len(s) and s[r + 1] == 'D':
                r += 1                
            
            ret[l:r+2] = reversed(ret[l:r+2])
            l = r + 1
            
        return ret

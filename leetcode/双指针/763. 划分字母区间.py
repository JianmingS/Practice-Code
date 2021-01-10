class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ret = []

        char_to_end = self.get_char_to_end(S)
        start = 0
        end = 0
        for i, ch in enumerate(S):
            end = max(end, char_to_end[ch])
            if i == end:
                ret.append(i - start + 1)
                start = i + 1
        
        return ret

    def get_char_to_end(self, s):
        ret = {}
        for i, ch in enumerate(s):
            ret[ch] = i
        return ret
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        char_list = [''] * len(indices)
        for index, val in enumerate(indices):
            char_list[val] = s[index]
        return ''.join(char_list)
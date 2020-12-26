class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        repeat_row_set = self.get_repeat_row_set(picture)
        repeat_col_set = self.get_repeat_col_set(picture)

        ret = 0
        for row_cnt, row in enumerate(picture):
            for col_cnt, col in enumerate(row):
                if picture[row_cnt][col_cnt] != 'B':
                    continue
                if row_cnt in repeat_row_set:
                    continue
                if col_cnt in repeat_col_set:
                    continue
                ret += 1
        
        return ret

    def get_repeat_row_set(self, picture):
        ret = set()
        for index, row in enumerate(picture):
            if row.count('B') > 1:
                ret.add(index)
        return ret

    def get_repeat_col_set(self, picture):
        ret = set()
        for col in range(len(picture[0])):
            ls = []
            for row in range(len(picture)):
                ls.append(picture[row][col])
            if ls.count('B') > 1:
                ret.add(col)
        return ret
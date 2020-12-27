class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        row_black_cnt = self.get_row_black_cnt_list(picture)
        col_black_cnt = self.get_col_black_cnt_list(picture)
        every_col_black_position = self.get_every_col_black_position(picture)

        legal_cnt = 0
        for row_index in range(len(picture)):
            if row_black_cnt[row_index] != N:
                continue
            for col_index in range(len(picture[0])):
                if col_black_cnt[col_index] != N:
                    continue
                if self.is_col_black_position_equal_row(row_index, every_col_black_position[col_index], picture):
                    legal_cnt += 1

        return legal_cnt

    def get_row_black_cnt_list(self, picture):
        ret = []
        for row in picture:
            ret.append(row.count('B'))
        return ret

    def get_col_black_cnt_list(self, picture):
        ret = []
        for col_index in range(len(picture[0])):
            cnt = 0
            for row_index in range(len(picture)):
                cnt += picture[row_index][col_index] == 'B' and 1 or 0
            ret.append(cnt)
        return ret

    def get_every_col_black_position(self, picture):
        ret = []
        for col_index in range(len(picture[0])):
            position_list = []
            for row_index in range(len(picture)):
                if picture[row_index][col_index] != 'B':
                    continue
                position_list.append(row_index)
            ret.append(position_list)
        return ret

    def is_col_black_position_equal_row(self, row_index, col_positon_list, picture):
        s = ''.join(picture[row_index])
        for col_positon in col_positon_list:
            if s != ''.join(picture[col_positon]):
                return False
        return True
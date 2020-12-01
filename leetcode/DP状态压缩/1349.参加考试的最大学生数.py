#
# @lc app=leetcode.cn id=1349 lang=python3
#
# [1349] 参加考试的最大学生数
#
# https://leetcode-cn.com/problems/maximum-students-taking-exam/description/
#
# algorithms
# Hard (46.15%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 4.7K
# Testcase Example:  '[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]'
#
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
# 
# 
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。
# 
# 学生必须坐在状况良好的座位上。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：seats = [["#",".","#","#",".","#"],
# [".","#","#","#","#","."],
# ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 
# 
# 
# 示例 2：
# 
# 输入：seats = [[".","#"],
# ["#","#"],
# ["#","."],
# ["#","#"],
# [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
# 
# 
# 示例 3：
# 
# 输入：seats = [["#",".",".",".","#"],
# [".","#",".","#","."],
# [".",".","#",".","."],
# [".","#",".","#","."],
# ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
# 
# 
# 
# 
# 提示：
# 
# 
# seats 只包含字符 '.' 和'#'
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.seats = []
        self.col_len = None
        self.row_len = None
        self.dp = None

    def maxStudents(self, seats: List[List[str]]) -> int:
        self.col_len = len(seats[0])
        self.row_len = len(seats)
        self.seats = self.getSeats(seats)
        self.dp = [[None]*self.row_len for i in range(1<<(self.col_len + 1))]
        return self.getMaxStudents(self.seats[0], 0)

    def getMaxStudents(self, seat, cur_row_num):
        if self.dp[seat][cur_row_num] is not None:
            return self.dp[seat][cur_row_num]

        max_val = 0

        for student in range(1<<self.col_len):
            if (student & (student << 1)) or (student & (~seat)):
                continue

            student_cnt = self.getStudentCnt(student)

            if cur_row_num == self.row_len - 1:
                max_val = max(max_val, student_cnt)
            else:
                next_seat = self.seats[cur_row_num + 1]
                next_seat &= ~(student >> 1)
                next_seat &= ~(student << 1)
                max_val = max(max_val, student_cnt + self.getMaxStudents(next_seat, cur_row_num + 1))
        
        self.dp[seat][cur_row_num] = max_val
        return max_val

    def getStudentCnt(self, student):
        student_cnt = 0
        while student:
            student_cnt += (student) & 1
            student >>= 1
        return student_cnt

    def getSeats(self, seats):
        ret = []

        for seat in seats:
            num = 0
            for i, s in enumerate(seat):
                if s == '.':
                    num |= (1 << (self.col_len - i - 1))
            ret.append(num)

        return ret

# @lc code=end


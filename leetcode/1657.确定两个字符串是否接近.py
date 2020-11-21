#
# @lc app=leetcode.cn id=1657 lang=python3
#
# [1657] 确定两个字符串是否接近
#
# https://leetcode-cn.com/problems/determine-if-two-strings-are-close/description/
#
# algorithms
# Medium (45.27%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 7.7K
# Testcase Example:  '"abc"\n"bca"'
#
# 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：
# 
# 
# 操作 1：交换任意两个 现有 字符。
# 
# 
# 例如，abcde -> aecdb
# 
# 
# 操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
# 
# 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
# 
# 
# 
# 
# 你可以根据需要对任意一个字符串多次使用这两种操作。
# 
# 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：word1 = "abc", word2 = "bca"
# 输出：true
# 解释：2 次操作从 word1 获得 word2 。
# 执行操作 1："abc" -> "acb"
# 执行操作 1："acb" -> "bca"
# 
# 
# 示例 2：
# 
# 
# 输入：word1 = "a", word2 = "aa"
# 输出：false
# 解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
# 
# 示例 3：
# 
# 
# 输入：word1 = "cabbba", word2 = "abbccc"
# 输出：true
# 解释：3 次操作从 word1 获得 word2 。
# 执行操作 1："cabbba" -> "caabbb"
# 执行操作 2："caabbb" -> "baaccc"
# 执行操作 2："baaccc" -> "abbccc"
# 
# 
# 示例 4：
# 
# 
# 输入：word1 = "cabbba", word2 = "aabbss"
# 输出：false
# 解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
# 
# 
# 
# 提示：
# 
# 
# 1 
# word1 和 word2 仅包含小写英文字母
# 
# 
#

# @lc code=start

import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1_char_to_cnt = collections.defaultdict(int)
        w2_char_to_cnt = collections.defaultdict(int)

        for char in word1:
            w1_char_to_cnt[char] += 1

        for char in word2:
            w2_char_to_cnt[char] += 1

        if set(w1_char_to_cnt.keys()) != set(w2_char_to_cnt.keys()):
            return False

        if sorted(w1_char_to_cnt.values()) != sorted(w2_char_to_cnt.values()):
            return False

        return True

# @lc code=end


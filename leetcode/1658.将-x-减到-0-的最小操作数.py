#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#
# https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (24.76%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 12.3K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要
# 修改 数组以供接下来的操作使用。
# 
# 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,4,2,3], x = 5
# 输出：2
# 解释：最佳解决方案是移除后两个元素，将 x 减到 0 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,6,7,8,9], x = 4
# 输出：-1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [3,2,20,1,1,3], x = 10
# 输出：5
# 解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        nums_len = len(nums)

        left_sum = 0
        left_sum_to_cnt_dic = {}
        for i in range(0, nums_len):
            left_sum += nums[i]
            if left_sum > x:
                break
            left_sum_to_cnt_dic[left_sum] = i+1

        right_sum = 0
        right_sum_to_cnt_dic = {}
        for i in range(nums_len-1, -1, -1):
            right_sum += nums[i]
            if right_sum > x:
                break
            right_sum_to_cnt_dic[right_sum] = nums_len - i

        ret = min(
            left_sum_to_cnt_dic.get(x) or float('INF'),
            right_sum_to_cnt_dic.get(x) or float('INF')
        )

        for left_sum, left_cnt in left_sum_to_cnt_dic.items():
            right_cnt = right_sum_to_cnt_dic.get(x-left_sum)
            if right_cnt is None:
                continue
            if right_cnt + left_cnt > nums_len:
                continue
            ret = min(ret, right_cnt + left_cnt)
        
        return ret == float('INF') and -1 or ret



        
# @lc code=end


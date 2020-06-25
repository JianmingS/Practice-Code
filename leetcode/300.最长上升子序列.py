import collections
from typing import List
import bisect

# class Solution:
#    def lengthOfLIS(self, nums: List[int]) -> int:
#        if not nums:
#            return 0
#
#        dp = [1] * len(nums)
#
#        for i in range(len(nums)):
#            for j in range(0, i):
#                if nums[j] < nums[i]:
#                    dp[i] = max(dp[i], dp[j] + 1)
#
#        return max(dp)
#


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ret = []

        for num in nums:
            if not ret or num > ret[-1]:
                ret.append(num)
                continue

            index = bisect.bisect_left(ret, num)
            # index = 0
            # l = 0
            # r = len(ret) - 1
            # while l <= r:
            #     middle = (l+r) >> 1
            #     if ret[middle] >= num:
            #         index = middle
            #         r = middle - 1
            #         continue

            #     l = middle + 1
            ret[index] = num

        # print(ret)
        return len(ret)


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    ls = [1, 3, 5]
    print(bisect.bisect_left(ls, 3))
    print(ls)

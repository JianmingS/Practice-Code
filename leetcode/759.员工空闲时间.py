# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        line_ls = []

        for ls in schedule:
            for item in ls:
                line_ls.append((item.start, '0'))
                line_ls.append((item.end, '1'))

        line_ls.sort(key=lambda item: (item[0], item[1]))
        ret = []
        balance = 0
        pre = None
        for v, v_type in line_ls:
            if balance == 0 and pre is not None:
                ret.append(Interval(pre, v))

            balance += (v_type == '0' and 1 or -1)
            pre = v

        return ret

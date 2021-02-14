# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        start_point = head
        end_point = head

        cnt = 0
        while start_point:
            start_point = start_point.next
            cnt += 1
            if cnt > k:
                end_point = end_point.next
        
        return end_point.val
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.kth = 0

    # 双指针
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode: 
        start_pointer = head
        end_pointer = head

        interval_cnt = 0
        while start_pointer:
            start_pointer = start_pointer.next
            interval_cnt += 1
            if interval_cnt > k:
                end_pointer = end_pointer.next

        return end_pointer

    # 递归
    def getKthFromEnd1(self, head: ListNode, k: int) -> ListNode:
        if head and head.next:
            node = self.getKthFromEnd(head.next, k)
            if self.kth == k:
                return node

        self.kth += 1
        return head

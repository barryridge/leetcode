#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2 and ((l1.val + l2.val) < 10):
            return ListNode((l1.val + l2.val) % 10, self.addTwoNumbers(l1.next, l2.next))
        elif l1 and l2:
            return ListNode((l1.val + l2.val) % 10, self.addTwoNumbers(self.addTwoNumbers(ListNode(1, None), l1.next), l2.next))
        elif l1:
            return ListNode(l1.val, l1.next)
        elif l2:
            return ListNode(l2.val, l2.next)
        else:
            return None

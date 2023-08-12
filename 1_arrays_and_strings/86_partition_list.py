from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr_small = small_head = ListNode(0)
        curr_large = large_head = ListNode(0)
        curr = head

        while curr:
            if curr.val < x:
                curr_small.next = curr
                curr_small = curr_small.next
            else:
                curr_large.next = curr
                curr_large = curr_large.next
            curr = curr.next

        curr_small.next = large_head.next
        return small_head.next
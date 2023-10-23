from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            if curr.val == val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next

        return dummy.next
            
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(888)
        dummy.next = head
        prev = dummy

        curr = head
        while curr:
            if curr.next is not None and curr.next.val == curr.val:
                while curr.next is not None and curr.next.val == curr.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev.next = curr
                prev = curr
            curr = curr.next
        return dummy.next
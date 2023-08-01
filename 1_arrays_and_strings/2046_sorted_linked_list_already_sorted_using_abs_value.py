from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        while curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                negative_node = curr.next
                curr.next = negative_node.next
                negative_node.next = head
                head = negative_node
        return head
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr_idx = 1
        total_length = 0
        start_node, end_node = None, None
        curr = head

        while curr:
            if curr_idx == k:
                start_node = curr
            curr_idx += 1
            total_length += 1
            curr = curr.next

        end_node = head
        for _ in range(total_length - k):
            end_node = end_node.next

        start_node.val, end_node.val = end_node.val, start_node.val

        return head
        

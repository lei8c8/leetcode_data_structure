from node import ListNode
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head

        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        
        return head
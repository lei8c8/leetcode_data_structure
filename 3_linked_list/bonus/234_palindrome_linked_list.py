from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        curr = head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans == ans[::-1]
    

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def find_middle(head):
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow if not fast else slow.next
        
        def reverse_second_half(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        middle_node = find_middle(head)
        first_half_head = head
        second_half_head = reverse_second_half(middle_node)
        while second_half_head:
            if second_half_head.val != first_half_head.val:
                return False
            first_half_head = first_half_head.next
            second_half_head = second_half_head.next
        return True

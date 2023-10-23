# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next

        base = 1
        ans = 0
        for i in range(len(lst) - 1, -1, -1):
            ans += lst[i] * base
            base *= 2
        return ans

        
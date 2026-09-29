# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = self.length(head)

        remove_index = N - n
        if remove_index == 0:
            return head.next

        i = 0
        cur = head
        while i < (remove_index - 1):
            cur = cur.next
            i += 1
        
        cur.next = cur.next.next
        return head
        
    def length(self, head: Optional[ListNode]) -> int:
        res = 0
        while head:
            res += 1
            head = head.next
        return res
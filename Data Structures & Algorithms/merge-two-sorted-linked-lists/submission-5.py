# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        res = ListNode()
        cur_res = res
        
        while cur1 or cur2:
            if not cur1:
                cur_res.next = cur2
                break
            elif not cur2:
                cur_res.next = cur1
                break

            if cur1.val < cur2.val:
                cur_res.next = cur1
                cur1 = cur1.next
            else:
                cur_res.next = cur2
                cur2 = cur2.next
            cur_res = cur_res.next

        return res.next
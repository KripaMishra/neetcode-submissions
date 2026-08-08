# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we will use two pointers, a slow and a fast one, 
        # we will move the slow pointer one place and fast one, two places. 
        # iff after moving they land on the same node then we return TRUE
        # the while loop is bounded by the fast and fast.next exist
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s ==f:
                return True
        return False

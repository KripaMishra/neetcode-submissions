# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode| None:
        # there will be three pointers: current value, .next, and last value.
        current = head
        prev  = None
        while current is not None:
            temp_next  = current.next
            current.next = prev
            prev = current
            current = temp_next
        
        return prev
        

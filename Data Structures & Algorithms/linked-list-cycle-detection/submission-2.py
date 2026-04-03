# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        # We must check both 'fast' and 'fast.next' to avoid crashes
        # because we are jumping 2 steps ahead.
        while fast and fast.next:

            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            if slow == fast:          # Collision! Cycle found.
                return True
                
        return False
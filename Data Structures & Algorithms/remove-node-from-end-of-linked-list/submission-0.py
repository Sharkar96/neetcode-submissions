# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count the nodes
        i = 0
        ptr = head
        while ptr:
            i += 1
            ptr = ptr.next

        # If n equals the total length, we are removing the head
        if i == n:
            return head.next

        # Traverse to the node *before* the one we want to delete
        ptr = head
        for _ in range(i - n - 1):
            ptr = ptr.next
        
        # Remove the target node
        ptr.next = ptr.next.next
        return head
            
        
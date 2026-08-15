# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cache = {}

        current = head
        while current != None:
            if current in cache:
                return True
            else:
                cache[current] = True
            
            current = current.next
        
        return False
        
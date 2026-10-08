# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the middle of the list

        slow = head
        if head != None: fast = head.next

        while fast != None:
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next

        middle = slow.next
        slow.next = None

        # 2. reverse second part of list
        reverse = None
        while middle != None:
            # save what will be the next middle
            tmp = middle.next

            # add the current element to the back 
            middle.next = reverse
            reverse = middle

            # advance pointer
            middle = tmp
        
        # 3. merge the two lists
        l1 = head
        l2 = reverse

        while l2 != None:
            tmp1 = l1.next
            tmp2 = l2.next

            # 1 2 3  # 6 5 4

            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2





            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head):
    prev = None
    

    while head:
        forward = head.next
        head.next = prev
        prev = head
        head = forward

    return prev

class Solution:
    



    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find the middle element first
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if fast:  #if the number of nodes is odd lets make the right portion small
            slow=slow.next
        #reversing the slow the right portion and compar it with the left portion
        slow= reverseList(slow)
        fast=head
        while slow:
            if slow.val!=fast.val:
                return False
            slow=slow.next
            fast=fast.next
        return True

    
    
     
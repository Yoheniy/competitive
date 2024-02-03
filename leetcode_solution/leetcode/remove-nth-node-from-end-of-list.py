# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        left=right=dummy
        current=dummy
        while n:
            right=right.next
            n-=1

        while right.next is not None:
            left=left.next
            right=right.next
        left.next=left.next.next
        print(left)

        return dummy.next
        
        

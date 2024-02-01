# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prevleft=dummy
        current=head
        temp=head
        for i in range(left-1):
            prevleft=prevleft.next
            current=current.next
        prev=None
        for i in range(right-left+1):
            next=current.next
            current.next=prev
            prev=current
            current=next
        prevleft.next=prev
        while prev.next:
            
            prev=prev.next
        prev.next=current


        return dummy.next

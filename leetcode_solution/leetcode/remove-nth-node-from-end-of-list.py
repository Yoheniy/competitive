# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cn=0
        temp=head
        while temp:
            cn+=1
            temp=temp.next
        pos=cn-n
        if pos==0:
            head=head.next
            return head
        current=head
        while current and (pos-1)!=0:
            pos-=1
            current=current.next
        current.next=current.next.next
        return head
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        if head is None:
            return
        current=head.next
        prev=head
        print(dummy)
        while current:
            if current.val>=prev.val:
                current,prev=current.next,prev.next
                continue
            temp=dummy
            while current.val>temp.next.val:
                temp=temp.next
            prev.next=current.next
            current.next=temp.next
            temp.next=current
            current=prev.next
            prev

        return dummy.next




                



        
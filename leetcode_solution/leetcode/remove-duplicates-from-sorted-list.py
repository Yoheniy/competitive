
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left=right=head
        
        while right and right.next:
            if right.val!=left.val:
                left.next=right
                left=left.next
            right=right.next
            if right.next is None and right.val==left.val:
                left.next=None
            else:
                left.next=right
            


        return head

        
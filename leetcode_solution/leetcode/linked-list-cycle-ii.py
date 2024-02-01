# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        meet=False

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next


            if slow==fast:
                meet=True
                break


        if meet:
            temp2=head
            while fast!=temp2:
                fast=fast.next
                temp2=temp2.next
            return fast


        
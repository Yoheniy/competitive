# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        if head.next==None:
            return head
        left=None
        right=None
        temp=head
        left2=right2=None
        while temp:
            if temp.val<x:
                if left == None:
                    left = ListNode(temp.val)
                    left2 = left
                else:
                    left2.next = ListNode(temp.val)
                    left2 = left2.next
              
            else:
                if right == None:
                    right = ListNode(temp.val)
                    right2 = right
                else:
                    right2.next = ListNode(temp.val)
                    right2 = right2.next
            temp = temp.next
        if left2 == None:
            return right
        left2.next = right
        
        return left

        

   
                    
        
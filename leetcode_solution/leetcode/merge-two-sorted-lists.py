
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(0)
        head=ans
   
        left=list1
        right=list2
        while left and right:

            if left.val>=right.val:
                newNode=ListNode(right.val)
                ans.next=newNode
                right=right.next
                ans=ans.next

            
            else:
                newNode=ListNode(left.val)
                ans.next=newNode
                ans=ans.next
                left=left.next
        if right:
            ans.next=right
        else:
            ans.next=left
            
            
        return head.next


        
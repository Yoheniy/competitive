# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #we have to modify the the given node to be deleted with the next value of node and link with the next of the nextnode 
        nextNode=node.next
        node.val=nextNode.val
        node.next=nextNode.next
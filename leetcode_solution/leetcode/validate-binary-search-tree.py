# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checker(node):
            nonlocal min_val
            if not node:
                return True 
            if not checker(node.left):
                return False
            if min_val>=node.val:
                return False
            min_val=node.val
            if not checker(node.right):
                return False
            return True
        min_val=float('-inf')
        return checker(root)
        
        
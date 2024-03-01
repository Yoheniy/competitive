# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=0
        def solve(node):
            nonlocal ans 
            if not node:
                return [-1,-1]
            left=solve(node.left)
            if left==[-1,-1]:
                left=[node.val,node.val]
            right=solve(node.right)
            if right==[-1,-1]:
                right=[node.val,node.val]
            ans=max(ans,abs(node.val-left[0]),abs(node.val-left[1]))
            ans=max(ans,abs(node.val-right[0]),abs(node.val-right[1]))
            return [min(left[0],right[0],node.val),max(left[1],right[1],node.val)]
        solve(root)
        return ans 

            
        
        
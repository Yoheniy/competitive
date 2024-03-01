# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=0
        def solve(node,q):
            nonlocal ans
            if not node:
                return q
            left=solve(node.left,q)-1
            if left==0:
                ans=node.val
            right=solve(node.right,left)
            return right
        solve(root,k)
        return ans



            
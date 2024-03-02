# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def solve(node):
            nonlocal ans 
            if not node:
                return
            if node.val>=low and node.val<=high:
                ans+=node.val
            solve(node.left)
            solve(node.right)
            return ans
        solve(root)
        return ans 
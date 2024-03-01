class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans=0
        def solve(node):
            nonlocal ans 
            if not node:
                return [0,float('inf'),float('-inf')]
            res=[0,float('inf'),float('-inf')]
            left=solve(node.left)
            right=solve(node.right)
            if left!='c' and right!='c' and left[2]<node.val and right[1]>node.val:
                res[0]+=node.val+right[0]+left[0]
                res[1]=min(res[1],node.val,left[1],right[1])
                res[2]=max(res[2],node.val,left[2],right[2])
            else:
                return 'c'
            ans=max(ans,res[0])
            return res 
        solve(root)
        return ans
            
            
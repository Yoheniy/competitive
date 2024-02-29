# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d=defaultdict(int)
        ans=[]
        def bfs(node):
            if not node:
                return 
            bfs(node.left)
            d[node.val]+=1
            bfs(node.right)
            return d
        arrlist=bfs(root)
        max_val=max(d.values())
        for key,val in d.items():
            if val==max_val:
                ans.append(key)
        return ans 
            

        

            
            
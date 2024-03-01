class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict_list=defaultdict(list)
        def zigzag(node,row):
            if not node:
                return
            dict_list[row].append(node.val)
            zigzag(node.left,row+1)
            zigzag(node.right,row+1)
            return dict_list

        zigzag(root,0)
        dict_list=dict(sorted(dict_list.items()))
        zigzag_list=[]
        k=0
        for val in dict_list.values():
            if k%2==0:
                zigzag_list.append(val)
            else:
                val.reverse()
                zigzag_list.append(val)
            k+=1
        return zigzag_list


       
        
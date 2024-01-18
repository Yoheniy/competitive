class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        ans=float('inf')
        cnwhite,left=0,0
        for right in range(len(blocks)):
            if blocks[right]=='W':
                cnwhite+=1
            if right-left+1==k:
                ans=min(ans,cnwhite)
                if blocks[left]=='W':
                    cnwhite-=1
                left+=1
        return ans 
        
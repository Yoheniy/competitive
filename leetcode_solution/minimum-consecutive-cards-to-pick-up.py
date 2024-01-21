class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left=0
        cn=Counter()
        ans=float("inf")
        ch=0
        for right in range(len(cards)):
            cn[cards[right]]+=1
            while cn[cards[right]]>1:

                ans=min(ans,right-left+1)
                cn[cards[left]]-=1
                left+=1
                ch=1
        if ch==0:
            return -1
                
        return ans



        '''map={}
        ans=float("inf")
        ch=0
        for i in range(len(cards)):
            if cards[i] in map:
                ans=min(ans,i-map[cards[i]])
                map[cards[i]]=i
                ch=1

                
            else:
                map[cards[i]]=i
        if ch==0:
            return -1
        return ans+1'''
        
        
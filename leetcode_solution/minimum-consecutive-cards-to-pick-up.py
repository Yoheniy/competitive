class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        map={}
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
        return ans+1
        
        
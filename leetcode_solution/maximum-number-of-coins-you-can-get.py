class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        # bob=[]
        # if len(piles)==3:
        #     return piles[1]
 
        # for i in range(len(piles)-2,-1,-2):
        #     bob.append(piles[i])
        # ans=sum(bob)-bob[len(bob)-1]
        n = len(piles)//3
        ans = 0
        for i in range(n,len(piles),+2):
            ans += piles[i]
        return ans

        
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans=[0]*len(deck)
        deck.sort()
        chance=flip=0
        q=deque()
        for i in range(len(deck)):
            q.append(i)
        while len(q)>0:
            if flip==0:
                ans[q[0]]=deck[chance]
                chance+=1
                q.popleft()
            else:
                q.append(q[0])
                q.popleft()
            flip^=1
        return ans 
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=[]
        one_loser=[]
        d={}
        s=set()
        for el in matches:
            d[el[1]]=d.get(el[1],0)+1
        for el in matches:
            s.add(el[0])
        
        for el in s:
            if d.get(el,0)==0:
                winner.append(el)
        for el in d:
            if d[el]==1:
                one_loser.append(el)
        one_loser.sort()
        winner.sort()
        l=[]
        l.append(winner)
        l.append(one_loser)
        return l        


        
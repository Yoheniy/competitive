class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={c:i for i,c in enumerate(order)}
        l=[]
        for word in words:
            l2=[]
            for _ in word:
                l2.append(dic[_])
            l.append(l2)
        for i in range(1,len(l)):
            if(l[i]<l[i-1]):
                return False
        return True



           


        
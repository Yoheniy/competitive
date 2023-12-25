class Solution:
    def printVertically(self, s: str) -> List[str]:
        ma=0
        words=s.split(" ")
        lch=[]
        for word in words:
            lch.append(list(word))
        
        for i in range(len(lch)):
            if(len(lch[i])>=ma):
                ma=len(lch[i])
                
        
        for i in range(len(lch)):
            
            diff=ma-len(lch[i])
            for _ in range(diff):
                lch[i].append(' ')
        ansch=[]
        for i in range(ma):
            temp=[]
            for j in range(len(lch)):
                if(i<len(lch[j])):
                    temp.append(lch[j][i])
            t="".join(temp)
            t=t.rstrip()
            ansch.append(t)

        
        return ansch
                



            

        
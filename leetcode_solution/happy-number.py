class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        l.append(n)
        while(n!=1):
            
            s=str(n)
            l1=[int(int(x)**2) for x in s]
            n=sum(l1)
            if n in l:
                return False
            else:
                l.append(n)
        return True
        


            
        
        
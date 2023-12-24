class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        total=0
        s=n
        l=[]
        
        while(n):
            cn=0
            mn=0
            while((n%(3**cn))==0):
                mn=cn
                cn+=1
            
            total+=(3**mn)
            l.append(3**mn)

            n= n-(3**mn)
        l1=list(set(l))
        if(total==s and len(l1)==len(l)):
            return True
        return False
        
    



        
        
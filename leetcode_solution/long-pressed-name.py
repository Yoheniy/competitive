class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l,r=0,0
        while r<len(typed):
            if l<len(name) and name[l]==typed[r]:
                l+=1
            elif r==0 or typed[r]!=typed[r-1]:
                return False
            r+=1




        return l==len(name)







        return True


                
            
            


            

        
        
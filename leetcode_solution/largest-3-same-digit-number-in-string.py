class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s=""
        b=""
        c=""
        for i in range(2,len(num)):
            if(num[i-2]==num[i-1]==num[i]):
                s+=num[i-2]
                s+=num[i-1]
                s+=num[i]
                b=max(b,s)
                s=""
               

            
        return b
             
            
            
        
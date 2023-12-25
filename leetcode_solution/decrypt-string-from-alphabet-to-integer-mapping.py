class Solution:
    def freqAlphabets(self, s: str) -> str:
        d=""
        nu=[x for x in range(26)]
        ch=[chr(x+97) for x in range(26)]
        i=0
        while(i<len(s)):
            if(i+2<len(s) and s[i+2]=='#'):
                temp=s[i:i+2]
                n=int(temp)
                d+=ch[n-1]
                i+=3
            else:
                temp=s[i]
                n=int(temp)
                d+=ch[n-1]
                i+=1
        return d
                
       

                    




        
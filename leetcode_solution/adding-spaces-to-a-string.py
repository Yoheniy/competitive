class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ll=list(s)
        d=s[:spaces[0]]
        for i in range(1,len(spaces)):
            j=spaces[i-1]
            temp=s[j:spaces[i]]
            d+=" "
            d+=temp
        d+=" "
        d+=s[spaces[len(spaces)-1]:]
        
        return d

        
        
        
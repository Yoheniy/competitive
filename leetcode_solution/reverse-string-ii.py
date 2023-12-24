class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        d=""
        i=0
        j=min(len(s),k)
        while(i<len(s)):
            d+=s[i:j][::-1]
            i+=2*k
            d+=s[j:i]
            j=min(i+k,len(s))
        return d
            
        
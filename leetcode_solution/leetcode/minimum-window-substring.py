class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=""
        tcounter=Counter(t)
        scounter=Counter(s[:len(t)-1])
        temp=float("inf")
        l=0
        r=len(t)-1
        while r<len(s):
            scounter[s[r]]+=1
            while tcounter-scounter==Counter():
                if r-l+1<temp:
                    temp=r-l+1
                    ans=s[l:r+1]
                scounter[s[l]]-=1
                
                l+=1
            r+=1
        return ans



        
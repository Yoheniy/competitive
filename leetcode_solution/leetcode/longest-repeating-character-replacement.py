class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m=Counter()
        l,ans=0,max(1,k)
    
        for r in range(len(s)):
            m[s[r]]+=1
            while (r-l+1)-max(m.values())>k:
                m[s[l]]-=1
    
                l+=1
            ans=max(ans,r-l+1)
        return ans 

        '''the brutforce one 
        def checker(s,chr):
            l,r=0,0
            ans,cn=0,0
            for r in range(len(s)):
                if s[r]!=chr:
                    cn+=1
                while cn>k:
                    if s[l]!=chr:
                        cn-=1
                    l+=1

                ans=max(ans,r-l+1)
            return ans 
        theans=0
        for i in range(len(s)):
            theans=max(theans,checker(s,s[i]))
        return theans
        '''




 


        
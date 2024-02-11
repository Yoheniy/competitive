class Solution:
    def minimumSteps(self, s: str) -> int:
        l=0
        cn=0
        for r in range(len(s)):
            if s[r]=='0':
                cn+=r-l
                l+=1
        
        return cn

        
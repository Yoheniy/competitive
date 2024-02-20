class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        cn=0
        for el in c:
            if c[el]%2!=0:
                cn+=1
        if cn==0 or cn==1:
            return len(s)
        return len(s)-cn+1

        
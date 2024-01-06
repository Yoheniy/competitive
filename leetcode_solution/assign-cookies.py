class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cn=0
        ans=[]
        i,j=0,0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                cn+=1
                s.remove(s[i])
                g.remove(g[j])
            else:
                s.remove(s[i])
        return cn
        
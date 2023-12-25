class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=list(s)
        j=0
        for i in indices:
            l[i]=s[j]
            j+=1
        d="".join(l)
        return d
        
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        l=list(s)
        d=list(set(l))
    

        return len(d)
        
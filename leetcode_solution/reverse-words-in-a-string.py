class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l.reverse()
        s=" ".join(l)
        s.strip()

        return s
        
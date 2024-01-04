class Solution:
    def sortSentence(self, s: str) -> str:
        ans=""
        l=[[int(t[-1]),t[:len(t)-1]] for t in s.split()]
        l.sort()
        ans=" ".join([word[1] for word in l])

        return ans
        
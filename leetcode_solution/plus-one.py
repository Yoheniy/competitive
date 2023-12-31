class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join([str(x) for x in digits])
        s+="+1"
        ans=eval(s)
        l=list(str(ans))
        l=[int(x) for x in l]

       
        return l
        
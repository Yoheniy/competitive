class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c={}
        ans=0
        for el in answers:
            if el==0:
                ans+=1
            else:
                if el not in c or el==c[el]:
                    c[el]=0
                    ans+=el+1
                else:
                    c[el]+=1
        return ans
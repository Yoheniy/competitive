class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        av=0.0
        sum=0
        cn=0
        for i in range(1,len(salary)-1):
            sum+=salary[i]
            cn+=1
        av=sum/cn
        return av

        
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        ans=0
        for key,value in c.items():
            temp=ceil(value/(key+1))
            ans+=(temp)*(key+1)
        return ans 
        #example we have [1,1,2]
        #our counter c={1:2,2:1}
        #1 element means other than me  there is 1 elements this means we are 2
        #2 element means other than me  there is 1 elements this means we are 3
        #the frequency element occur division by the number of that group it give us in how many group we divide them
        #and multiplication of the amount of group and the total number of element in the group gives us the answer
        

        
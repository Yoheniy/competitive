class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        l=[]
        total=sum(x for x in nums if x%2==0)
        for el in queries:
            temp=nums[el[1]]
            
            if(temp%2==0 and el[0]%2==0):
                nums[el[1]]+=el[0]
                total+=el[0]
                l.append(total)
                
            elif(temp%2==0 and el[0]%2!=0):
                nums[el[1]]+=el[0]
                total-=temp
                l.append(total)
            elif(temp%2!=0 and el[0]%2!=0):
                nums[el[1]]+=el[0]
                total+=el[0]+temp
                l.append(total)
            else:
                nums[el[1]]+=el[0]
            
                l.append(total)                            

           
            
        return l


        
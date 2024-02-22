class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans=0
        Yprefixsum=[0]
        Nprefixsum=[0]
        for i in range(len(customers)):
            if customers[i]=="Y":
                Yprefixsum.append(Yprefixsum[-1]+1)
                Nprefixsum.append(Nprefixsum[-1])
            else:
                Yprefixsum.append(Yprefixsum[-1])
                Nprefixsum.append(Nprefixsum[-1]+1)
        prev=float("inf")
        for i in range(len(Yprefixsum)):
            curr=Yprefixsum[-1]-Yprefixsum[i]+Nprefixsum[i]
            if curr<prev:
                ans=i
                prev=curr
        return ans 




        
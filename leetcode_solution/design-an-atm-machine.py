class ATM:

    def __init__(self):
        self.count=[0]*5
        self.money=[20,50,100,200,500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.count[i]+=banknotesCount[i]
        
        

    def withdraw(self, amount: int) -> List[int]:
        ans=[0]*5
        for j in range(4,-1,-1):
            temp=amount//self.money[j]
            if temp>self.count[j]:
                temp=self.count[j]
            ans[j]=temp
            amount-=temp*self.money[j]
        if amount!=0:
            return [-1]
        for i in range(len(self.count)):
            self.count[i]-=ans[i]
        return ans

            


        
       
            

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
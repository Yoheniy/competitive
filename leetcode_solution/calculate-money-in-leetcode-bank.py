class Solution:
    def totalMoney(self, n: int) -> int:
        q=n//7
        rem=abs(n-(7*q))
        return int((q*28)+(((q-1)*q*7)/2)+((rem*(rem+1))/2)+(rem*q))

            


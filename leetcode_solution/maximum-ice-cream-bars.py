class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total=sum(costs)
        cn=len(costs)
        while total>coins:
            cn-=1
            total-=costs[cn]

        return cn
            
    



        
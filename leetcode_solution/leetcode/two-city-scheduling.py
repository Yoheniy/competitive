class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])
      
        num_people = len(costs) // 2 

        total_cost = sum(costs[i][0] for i in range(num_people)) + \
                     sum(costs[i + num_people][1] for i in range(num_people))
      
        return total_cost
        
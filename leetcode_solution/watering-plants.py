class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water=capacity
        cn=0
        i=0
        while i<len(plants):
            if water>=plants[i]:
                cn+=1
                water-=plants[i]
                i+=1
            else:
                water=capacity
                cn+=2*i+1
                water-=plants[i]
                i+=1
      
        return cn


        
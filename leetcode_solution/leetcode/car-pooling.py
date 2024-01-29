class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix=[0]*1001
        for el in trips:

            prefix[el[1]]+=el[0]
            prefix[el[2]]-=el[0]
        total=0
        for i in range(len(prefix)):
           total+=prefix[i]
           if total>capacity:
               return False
        return True
    



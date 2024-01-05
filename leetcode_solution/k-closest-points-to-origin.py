class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        em=[]
        for el in points:
            temp=(el[0])**2 + (el[1])**2
            l.append(temp)
        print(l)
        em=list(zip(l,points))
        print(em)
        em.sort()
        ans=[]
        for i in range(k):
            ans.append(em[i][1])
        return ans
        

            


        
        return 0

        
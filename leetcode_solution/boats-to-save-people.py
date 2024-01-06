class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right=0,len(people)-1
        ans=0
        while left<right:
            if people[left]+people[right]<=limit:
                people[left]=0
                people[right]=0
                ans+=1
                right-=1
                left+=1
                
            elif people[left]+people[right]>limit:

                right-=1
            else:
                left+=1

        for el in people:
            if el!=0:
                ans+=1
        return ans
        
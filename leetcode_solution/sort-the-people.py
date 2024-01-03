class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair={}
        ans=[]
        i=0
        for el in heights:
            pair[el]=i
            i+=1
        sortedpair=dict(sorted(pair.items(),reverse=True))
        for el in sortedpair:
            temp=sortedpair[el]
            ans.append(names[temp])

        return ans
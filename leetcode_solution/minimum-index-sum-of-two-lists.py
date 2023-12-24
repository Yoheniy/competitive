class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        for i,el in enumerate(list1):
            dic[el]=i
        l=[]
        mn=sys.maxsize
        for j in range(len(list2)):
            if list2[j] in dic:
                total=j+dic[list2[j]]
                if total<mn:
                    l.clear()
                    l.append(list2[j])
                    mn=total
                elif(total==mn):
                    l.append(list2[j])
        return l

                   
        
                    
        
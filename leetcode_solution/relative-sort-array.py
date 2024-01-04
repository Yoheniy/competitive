class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=list(set(arr1)-set(arr2))
        

        
        mp=Counter(arr1)
        l=[]
        print(mp)
        for el in arr2:
            for i in range(mp[el]):
                l.append(el)
        print(l)
        l1=[]
        for el in d:
            for i in range(mp[el]):
                l1.append(el)
        l1.sort()
        l.extend(l1)
        
        return l
        
        
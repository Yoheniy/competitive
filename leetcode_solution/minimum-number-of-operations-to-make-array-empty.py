class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for el in nums:
            d[el]+=1
        cn=0
        if 1 in d.values():
            return -1
        for el in d:
            print(el,d[el])
            if d[el]%3==2:
                cn+=d[el]//3
                cn+=1 
            
            elif d[el]%3!=1:
                print(d[el])
                cn+=d[el]//3
                print(cn)
    
                 
            else:
                cn+=d[el]//3
                cn+=1
                print(cn)
      
        return cn
        
import random
class RandomizedSet:
   
    def __init__(self):
        self.myset=[]
        self.index={}
        self.i=0

    def insert(self, val: int) -> bool:
        if val not in self.myset:
            self.myset.append(val)
            self.index[val]=self.i
            self.i+=1
            return True
        return False
      
    def remove(self, val: int) -> bool:
        if val in self.index:

            indx=self.index[val]
            self.index[self.myset[-1]]=indx
            self.myset[indx],self.myset[-1]=self.myset[-1],self.myset[indx]
            
            self.myset.pop()
            self.index.pop(val)
            self.i-=1
            return True
        return False
        

    def getRandom(self) -> int:
        
        return random.choice(self.myset)
        
        
       
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
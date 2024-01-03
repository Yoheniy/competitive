class Bitset:

    def __init__(self, size: int):
        self.bitset=[0]*size
        self.flipped=[1]*size
        self.cn1=0
        
        

    def fix(self, idx: int) -> None:
        if self.bitset[idx]==0:
            self.bitset[idx]=1
            self.cn1+=1
            self.flipped[idx]=0
        
    def unfix(self, idx: int) -> None:
        if self.bitset[idx]==1:
            self.bitset[idx]=0
            self.cn1-=1
            self.flipped[idx]=1
        

    def flip(self) -> None:
        self.bitset,self.flipped=self.flipped,self.bitset
        self.cn1=len(self.bitset)-self.cn1
            
    def all(self) -> bool:
        return self.cn1==len(self.bitset)


    
    def one(self) -> bool:
        return self.cn1>0
        
    def count(self) -> int:
   
        return self.cn1
        

    def toString(self) -> str:
        string="".join([str(x) for x in self.bitset])
        return string
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
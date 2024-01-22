class Robot:
    

    def __init__(self, width: int, height: int):
        self.x=0
        self.y=0
        self.w=width
        self.h=height
        self.dx,self.dy=1,0
        self.par=(2*self.w)+(2*self.h)-4
    def multi(self):
        if self.x>=self.w:
            self.y=(self.x-self.w)+1
            self.x=self.w-1
            self.dx=0
            self.dy=1
        if self.y>=self.h:
            self.x-=(self.y-self.h)+1
            self.y=self.h-1
            self.dx=-1
            self.dy=0
        if self.x<0:
            self.y-=0-self.x
            self.x=0
            self.dx=0
            self.dy=-1
        if self.y<0:
            self.x+=0-self.y
            self.y=0
            self.dy=0
            self.dx=1
        
        
    def step(self, num: int) -> None:
        d=num%self.par
        if self.x==0 and self.y==0 and num//self.par>0:
            self.dx=0
            self.dy=-1
        elif  self.x==self.w-1 and self.y==0 and num//self.par>0:
            self.dx=1
            self.dy=0
        elif  self.x==0 and self.y==self.h-1 and num//self.par>0:
            self.dx=-1
            self.dy=0
        elif self.x==self.w-1 and self.y==self.h-1 and num//self.par>0:
            self.dx=0
            self.dy=1
        self.x+=self.dx*d
        self.y+=self.dy*d
        while self.x>=self.w or self.y>=self.h or self.y<0 or self.x<0:
            self.multi()


        

    def getPos(self) -> List[int]:
        return [self.x,self.y]
        

    def getDir(self) -> str:
        if self.dx==1:
            return "East"
        elif self.dy==1:
            return "North"
        elif self.dx==-1:
            return "West"
        else:
            return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
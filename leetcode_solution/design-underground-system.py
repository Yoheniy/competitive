class UndergroundSystem:

    def __init__(self):
        self.checkin=defaultdict()
        self.ans=defaultdict()
        
        

    def checkIn(self, id: int, stationName: str, t: int)-> None:

         
        self.checkin[id]=[stationName,t]
        

    def checkOut(self, id: int, end: str, tend: int) -> None:
        start,tstart=self.checkin[id]
        if (start,end) not in self.ans:
            self.ans[(start,end)]=[0,0]
        self.ans[(start,end)][0]+=tend-tstart
        self.ans[(start,end)][1]+=1

        


        

    def getAverageTime(self, start: str, end: str) -> float:
        total,count=self.ans[(start,end)]
        return total/count
        
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
class FrequencyTracker:

    def __init__(self):
        self.coll=collections.defaultdict(int)
        self.freq=collections.defaultdict(int)

    def add(self, number: int) -> None:
        
        self.coll[number]+=1
        prev=self.coll[number]
        self.freq[prev]+=1
        self.freq[prev-1]-=1
        

    def deleteOne(self, number: int) -> None:
        if self.coll[number]>0:
            self.coll[number]-=1
            prev=self.coll[number]
            self.freq[prev]+=1
            self.freq[prev+1]-=1
    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]>=1
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
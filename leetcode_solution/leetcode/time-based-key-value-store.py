class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        temp=self.d[key]
        left,right=0,len(temp)-1
        best=''
        while left<=right:
            mid=left+(right-left)//2
            if temp[mid][0]>timestamp:
                right=mid-1
            else:
                best=temp[mid][1]
                left=mid+1
        return best
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
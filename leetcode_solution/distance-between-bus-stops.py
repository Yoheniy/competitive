class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
       
        if start>destination:
            temp=start
            start=destination
            destination=temp
        clockwise,cnclockwise=0,0
        for i in range(len(distance)):
            if i>=start and i<destination:
                clockwise+=distance[i]
            else:
                cnclockwise+=distance[i]

        return min(clockwise,cnclockwise)
            
        
        
        
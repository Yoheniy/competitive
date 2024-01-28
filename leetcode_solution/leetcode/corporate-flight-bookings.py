class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ps=[0]*n
        for i in range(len(bookings)):
            l,r,k=bookings[i][0],bookings[i][1],bookings[i][2]
            if r<n:
                ps[l-1]+=k
                ps[r]-=k
            else:
                ps[l-1]+=k
        prefix=[0]*n
        prefix[0]=ps[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+ps[i]
        return prefix


        
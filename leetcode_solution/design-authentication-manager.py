class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.pair={}
        self.timetolive=timeToLive
        


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.pair[tokenId]=currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.pair:
            if self.pair[tokenId]+self.timetolive>currentTime:
                self.pair[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cn=0
        for el in self.pair:
            if self.pair[el]+self.timetolive>currentTime:
                cn+=1
        return cn


        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
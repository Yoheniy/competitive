class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times=times
        count=Counter()
        self.winnerboard=[]
        curr_win=persons[0]
        for i in range(len(persons)):
            count[persons[i]]+=1
            if count[persons[i]]>=count[curr_win]:
                curr_win=persons[i]
            self.winnerboard.append(curr_win)

    def q(self, t: int) -> int:
        index=bisect_right(self.times,t)
        return self.winnerboard[index-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
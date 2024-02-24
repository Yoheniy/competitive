class RecentCounter:

    def __init__(self):
        self.q=deque()
    def ping(self, t: int) -> int:
        temp=t-3000
        self.q.append(t)
        while self.q[0]<temp:
            self.q.popleft()
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
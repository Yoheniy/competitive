class MinStack:

    def __init__(self):
        self.stack1=[]
        self.minstack=[]
    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            _min=min(val,self.minstack[-1])
            self.minstack.append(_min)
    def pop(self) -> None:
        if self.stack1:
            self.stack1.pop()
        if self.minstack:
            self.minstack.pop()
    def top(self) -> int:
        return self.stack1[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MyStack:
    def __init__(self):
        self.MyStack=[]
    def push(self, x: int) -> None:
        self.MyStack.append(x)
    def pop(self) -> int:
        if MyStack:
            temp=self.MyStack[-1]
            self.MyStack.pop()
        return temp  
    def top(self) -> int:
        if not self.MyStack:
            return -1
        return self.MyStack[-1]
    def empty(self) -> bool:
        return not self.MyStack
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
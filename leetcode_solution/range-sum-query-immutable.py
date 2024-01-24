class NumArray:

    def __init__(self, nums: List[int]):
        self.num=nums
        self.prevsum=[0]
        for i in range(len(self.num)):
            x=self.prevsum[-1]+self.num[i]
            self.prevsum.append(x)
        
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prevsum[right+1]-self.prevsum[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
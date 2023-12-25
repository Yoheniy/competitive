class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        for i in range(n):
            l.append(nums[i])
            i+=n
            l.append(nums[i])
            i-=n
        return l
        
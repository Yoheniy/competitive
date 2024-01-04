class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        inf=10**23
        small,mid=inf,inf
        for n in nums:
            if n<=small:
                small=n
            elif n<=mid:
                mid=n
            else:
                return True
                
        return False
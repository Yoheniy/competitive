class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cn=0
        for _ in range(len(nums)):
            for j in range( _+1,len(nums)):
                if(nums[_]==nums[j]):
                    if((_*j)%k==0):
                        cn=cn+1
        return cn

        
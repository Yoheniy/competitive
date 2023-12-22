class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cn=0
        mx=-10000000000
        r=0
        l=0
        while(r<len(nums)):
            if(nums[r]==1):
                r+=1
                cn+=1
            else:
                temp=r-l
                cn=0
                mx=max(mx,temp) 
                r+=1
                l=r  
            mx=max(mx,cn)         
           
        return mx
            

        